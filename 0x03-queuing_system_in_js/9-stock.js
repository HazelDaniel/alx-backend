#!/usr/bin/node
import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();
const PORT = 1245;
const HOST = '127.0.0.1';
const listProducts = [{
  id: 1, name: 'Suitcase 250', price: 50, stock: 4,
},
{
  id: 2, name: 'Suitcase 450', price: 100, stock: 10,
},
{
  id: 3, name: 'Suitcase 650', price: 350, stock: 2,
},
{
  id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
},
];

/**
 * uses the provided id parameter to Search for a product in the listProducts array
 * @param {number} id - product's id
 * @returns {object} - product object if found, otherwise undefined
 */
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

// Redis client ops
client.on('error', (error) => {
  console.log(`Redis client not connected to server ${error.message}`);
});

/**
 * Sets a itemId-stock key-value pair in redis store
 * @param {string} itemId - item id
 * @param {number} stock - product stock
 */
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

/**
 * Gets stock value associated with given item id (as key)
 * from the redis store
 * @param {string} itemId - product's id
 * @returns {(string | null)} - current stock of products
 */
async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const value = await getAsync(`item.${itemId}`);
  return value;
}

// Express app routes
app.get('/list_products', (_req, res) => {

  res.send(listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  })));
});

app.get('/list_products/:itemId', async (req, res) => {

  const { itemId } = req.params;
  const product = getItemById(Number(itemId));

  if (product === undefined) {
    res.statusCode = 404;
    res.send({ status: 'Product not found' });
  } else {
    const reserveStock = await getCurrentReservedStockById(product.id);
    res.send({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity: reserveStock === null ? product.stock : Number(reserveStock),
    });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));

  if (product === undefined) {
    res.statusCode = 404;
    res.send({ status: 'Product not found' });
    return;
  }

  let reserveStock = await getCurrentReservedStockById(product.id);

  reserveStock = reserveStock === null ? product.stock : Number(reserveStock);
  if (!reserveStock) {
    res.send({ status: 'Not enough stock available', ItemId: product.id });
  } else {
    reserveStockById(product.id, reserveStock - 1);
    res.send({ status: 'Reservation confirmed', ItemId: product.id });
  }
});

app.listen(PORT, HOST, () => {
  console.log(`Server is live at ${HOST}:${PORT}`);
});

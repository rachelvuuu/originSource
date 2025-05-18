export const config = { api: { bodyParser: false } };

export default async function handler(req, res) {
  let body = Buffer.from([]);
  for await (const chunk of req) {
    await new Promise(resolve => setTimeout(resolve, 3000));
    body = Buffer.concat([body, chunk]);
  }
  res.status(200).send(`Origin Send Timeout simulation received body: ${body.toString()}`);
}
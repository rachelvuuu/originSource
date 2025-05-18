export default async function handler(req, res) {
  const time = parseInt(req.query.time || "10", 10);
  await new Promise(resolve => setTimeout(resolve, time * 1000));
  res.status(200).send(`Client Header Delay of ${time}s completed.`);
}
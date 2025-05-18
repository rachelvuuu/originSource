export default async function handler(req, res) {
  res.status(504).send("Simulated Origin Connect Timeout (Gateway Timeout)");
}
module.exports = (req, res) => {

  console.log(process.env.TEST_VAR)

  const date = new Date().toString();
  res.status(200).send(date);
};

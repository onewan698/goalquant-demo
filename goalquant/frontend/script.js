async function getPoisson(lambda) {
  const res = await fetch(`/api/poisson?lambda=${lambda}`);
  const data = await res.json();
  // 显示数据
}

async function getKelly(prob, odds) {
  const res = await fetch(`/api/kelly?prob=${prob}&odds=${odds}`);
  const data = await res.json();
  // 显示数据
}

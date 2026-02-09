function gera_cor(qtd) {
  qtd = qtd || 1;
  var bg_color = [];
  var border_color = [];
  for (var i = 0; i < qtd; i++) {
    var r = Math.random() * 255;
    var g = Math.random() * 255;
    var b = Math.random() * 255;
    bg_color.push("rgba(" + r + ", " + g + ", " + b + ", 0.2)");
    border_color.push("rgba(" + r + ", " + g + ", " + b + ", 1)");
  }
  return [bg_color, border_color];
}

function renderiza_total_vendido(url) {
  fetch(url, { method: "get" })
    .then(function (r) { return r.json(); })
    .then(function (data) {
      document.getElementById("faturamento_total").innerHTML = data.total;
    });
}

function renderiza_faturamento_mensal(url) {
  fetch(url, { method: "get" })
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var ctx = document.getElementById("faturamento_mensal").getContext("2d");
      var cores = gera_cor(12);
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.labels,
          datasets: [{
            label: "Faturamento",
            data: data.data,
            backgroundColor: cores[0],
            borderColor: cores[1],
            borderWidth: 1
          }]
        },
        options: { scales: { y: { beginAtZero: true } } }
      });
    });
}

function renderiza_despesas_mensal() {
  var ctx = document.getElementById("despesas_mensal").getContext("2d");
  var cores = gera_cor(12);
  new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
      datasets: [{
        label: "Despesas",
        data: [12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3],
        backgroundColor: "#CB1EA8",
        borderColor: "#FFFFFF",
        borderWidth: 0.2
      }]
    }
  });
}

function renderiza_produtos_mais_vendidos(url) {
  fetch(url, { method: "get" })
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var ctx = document.getElementById("produtos_mais_vendidos").getContext("2d");
      var cores = gera_cor(4);
      new Chart(ctx, {
        type: "doughnut",
        data: {
          labels: data.labels,
          datasets: [{
            data: data.data,
            backgroundColor: cores[0],
            borderColor: cores[1],
            borderWidth: 1
          }]
        }
      });
    });
}

function renderiza_funcionario_mes(url) {
  fetch(url, { method: "get" })
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var ctx = document.getElementById("funcionarios_do_mes").getContext("2d");
      var cores = gera_cor(4);
      new Chart(ctx, {
        type: "polarArea",
        data: {
          labels: data.labels,
          datasets: [{
            data: data.data,
            backgroundColor: cores[0],
            borderColor: cores[1],
            borderWidth: 1
          }]
        }
      });
    });
}

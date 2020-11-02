function charts(ativo,encerrados){

    var brandPrimary = '#33b35a';
    var PIECHART = $('#pieChart');
    var myPieChart = new Chart(PIECHART, {
        type: 'doughnut',
        data: {
            labels: [
                "Ativos",
                "Encerrados",
            ],
            datasets: [
                {
                    data: [ativo,encerrados],
                    borderWidth: [1, 1],
                    backgroundColor: [
                        brandPrimary,
                        "rgba(75,192,192,1)",
                        "#FFCE56"
                    ],
                    hoverBackgroundColor: [
                        brandPrimary,
                        "rgba(75,192,192,1)",
                        "#FFCE56"
                    ]
                }]
        }
    });
};

//

function charts2(manutencao,agua,eletricidade,imposto,outros){

    var brandPrimary = '#33b35a';
    var PIECHART = $('#pieChart2');
    var myPieChart = new Chart(PIECHART, {
        type: 'doughnut',
        data: {
            labels: [
                "Manutenções",
                "Água",
                "Eletricidade",
                "Impostos",
                "Outros",

            ],
            datasets: [
                {
                    data: [manutencao,agua,eletricidade,imposto,outros],
                    borderWidth: [1, 1],
                    backgroundColor: [
                        brandPrimary,
                        "rgba(75,192,192,1)",
                        "#FFCE56",
                        "#CD853F"
                    ],
                    hoverBackgroundColor: [
                        brandPrimary,
                        "rgba(75,192,192,1)",
                        "#FFCE56",
                        "#CD853F"
                    ]
                }]
        }
    });
};


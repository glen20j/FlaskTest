$(function () {

    Accuracy_BarChart();

    $(".dropdown-menu li a").click(function () {

        var id = $(this).closest('div').attr('id')
        if (id == "DD_Accuracy_BarChart") {
            //set the dropdown new text
            document.getElementById("Accuracy").innerHTML = $(this).text();
            Accuracy_BarChart()
        }

    });
});

function Accuracy_BarChart() {

    $.ajax({
        type: "POST",
        url: "/accuracybarchart",
        data: { filtertype_Accuracy: String($("#Accuracy").text()) },
        dataType: "json",
        success: function (response) {

            $("#Accuracy_BarChart").html("");
            var el = document.createElement('canvas');
            $("#Accuracy_BarChart")[0].appendChild(el);


            if (response["data"] != "]") {



                var Data_Accuracy_BarChart = eval(response["data"]);
                var BackgroundColor_Accuracy_BarChart = eval(response["backgroundcolor"]);
                var Labels_Accuracy_BarChart = eval(response["labels"]);

                var data = {
                    labels: Labels_Accuracy_BarChart,
                    datasets: [{
                        data: Data_Accuracy_BarChart,
                        backgroundColor: BackgroundColor_Accuracy_BarChart
                    }]
                };

                var options = {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: 'Model data accuracy by team'
                    },
                    scales: {
                        xAxes: [{
                            stacked: false,
                            beginAtZero: true,
                            //scaleLabel: {
                            //            labelString: 'Month'
                            //            },
                            ticks: {
                                autoSkip: false,
                                maxRotation: 90,
                                minRotation: 90
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                //callback: function (value, index, values) {
                                //    if (parseInt(value) >= 1000) {
                                //        return '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                                //    } else {
                                //        return '$' + value;
                                //    }
                                //}
                            }
                        }]
                    },
                    tooltips: {
                        callbacks: {
                            //label: function (tooltipItem, data) {
                            //    //get the concerned dataset
                            //    var dataset = data.datasets[tooltipItem.datasetIndex];
                            //    //calculate the total of this data set
                            //    var total = dataset.data.reduce(function (previousValue, currentValue, currentIndex, array) {
                            //        return previousValue + currentValue;
                            //    });
                            //    //get the current items value
                            //    var currentValue = dataset.data[tooltipItem.index];
                            //    var currentLabel = Labels_Accuracy_BarChart[tooltipItem.index];

                            //    //calculate the precentage based on the total and current item, also this does a rough rounding to give a whole number
                            //    //var precentage = Math.floor(((currentValue / total) * 100) + 0.5);

                            //    //return precentage + "%";

                            //    return '$' + currentValue.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,');

                            //    //var multistring = [currentLabel];
                            //    //multistring.push('$' + currentValue.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,'));

                            //    //return multistring;
                            //    //return currentLabel + "\n" + '$' + currentValue.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,');
                            //}
                        }
                    }

                };

                var ctx = el.getContext('2d');
                ctx.canvas.width = 300;
                ctx.canvas.height = 120;

                var Accuracy_BarChart = new Chart(ctx, {
                    type: 'bar',
                    data: data,
                    options: options

                });

            }

        },
        failure: function (response) {
            alert('There was an error.');
        }
    });
};
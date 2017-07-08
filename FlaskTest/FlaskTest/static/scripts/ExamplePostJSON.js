var data = {
    "sport": {
        "channel": "Seven",
        "timeslot": {
            "location": "Melbourne",
            "datetime": "2012-04-23T18:25:43.511Z",
            "team": "Essendon"
        },
        "statistics": {
            "gamecount": "4",
            "homeaway": "away",
            "accuracy": "45"
        }
    }
}

var get_data = {
    "constraint_data": {
        "constraint1_flt": 321.0,
        "constraint2_bool": true,
        "constraint3_str": "fds",
        "constraint4_sel": "text",
        "constraint5_selmult": "Essendon",
        "constraint6_txtarea": "test",
        "constraint7_decimal": 324.0,
        "createddate": [
          "2017-07-07",
          "00:08:29"
        ]
    }
}

document.getElementById("JSON_ExamplePost").innerHTML = JSON.stringify(data, undefined, 2);
document.getElementById("JSON_ExampleGet").innerHTML = JSON.stringify(get_data, undefined, 2);
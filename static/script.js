function predict() {
    const data = {
        start_position: Number(document.getElementById("start_position").value),
        grid_normalized: Number(document.getElementById("grid_normalized").value),
        driver_avg_finish: Number(document.getElementById("driver_avg_finish").value),
        race_difficulty: Number(document.getElementById("race_difficulty").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").innerText =
            "Predicted Finish Position: " + result.predicted_finish_position;
    })
    .catch(error => {
        console.error(error);
    });
}

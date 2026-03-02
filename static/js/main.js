document.getElementById("features_form").addEventListener("submit",async function(e){
    e.preventDefault();

    const form_data = new FormData(this);

    const data = {
        engine_rpm: Number(form_data.get("engine_rpm")),
        lub_oil_pressure: Number(form_data.get("lub_oil_pressure")),
        fuel_pressure: Number(form_data.get("fuel_pressure")),
        coolant_pressure: Number(form_data.get("coolant_pressure")),
        lub_oil_temp: Number(form_data.get("lub_oil_temp")),
        coolant_temp: Number(form_data.get("coolant_temp"))
    };

    console.log(data)
    // setTimeout(()=>{console.log("closing")}, 6000)

    const response = await fetch("/predict", {
        method:"POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify(data)
    })

    const result = await response.json();
    const condition = result.prediction == 1 ? "Healthy" : "Unhealthy"

    const engCondLabel = document.getElementById("engine_condition")
    engCondLabel.style.color =  result.prediction == 1 ? "green" : "red"
    engCondLabel.textContent = `Engine Condition  ${condition}`
})

document.querySelector("#button").onclick = async function calculateValue() {
    console.log("loading model")
    const model = await tf.loadLayersModel('src/model/model.json');
    let value1 = parseFloat(document.getElementById("margini").value);
    let value2 = parseFloat(document.getElementById("HPV").value);
    let value3 = parseFloat(document.getElementById("NL").value);
    console.log(value1);
    console.log(value2);
    console.log(value3);

    console.log("evaluating");
    document.getElementById("demo").innerHTML = model.predict(tf.tensor1d([value1, value2, value3]).expandDims()).arraySync()[0][0];
}
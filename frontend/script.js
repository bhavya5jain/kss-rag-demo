document.getElementById('instructionForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the default form submission

    const rawInstructionDiv = document.getElementById("rawInstruction");
    rawInstructionDiv.innerHTML = "";
    const explanationDiv = document.getElementById("explanation");
    explanationDiv.innerHTML = "";
    const exampleDiv = document.getElementById("example");
    exampleDiv.innerHTML = "";
    const contextInformationDiv = document.getElementById("contextInformation");
    contextInformationDiv.innerHTML = "";

    const instructionValue = document.getElementById('instruction').value;

    var backend_endpoint = `http://localhost:5000/assembler_description?instruction=${instructionValue}`;
    fetch(backend_endpoint)
    .then(response => response.json())
    .then(data => {
        rawInstructionDiv.innerHTML += "<h2>Instruction</h2>";
        rawInstructionDiv.innerHTML += instructionValue + "<br>";

        explanationDiv.innerHTML += "<h2>Brief explanation</h2>";
        explanationDiv.innerHTML += data.shortDescription + "<br>";

        exampleDiv.innerHTML += "<h2>Example usage</h2>";
        exampleDiv.innerHTML += data.example + "<br>";

        contextInformationDiv.innerHTML += "<h2>IBM Principle of operations page labels</h2>";
        contextInformationDiv.innerHTML += data.contextInformation + "<br>";
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('response').textContent = 'Error: ' + error;
    });
});


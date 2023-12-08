window.onload = function () {
    // Set default values if the input field is empty
    let gen01 = document.getElementById('gen01').value;
    if (!gen01) {
        gen01 = "3, 5"; // Default value
        document.getElementById('gen01').value = gen01; // Update the input field with default values
    }
    calculateSemigroup();

    let gen02 = document.getElementById('gen02').value;
    if (!gen02) {
        gen02 = "3, 5"; // Default value
        document.getElementById('gen02').value = gen02; // Update the input field with default values
    }

    let element01 = document.getElementById('element01').value;
    if (!element01) {
        element01 = "42"; // Default value
        document.getElementById('element01').value = element01; // Update the input field with default values
    }

    calculateFactorizationLengths();

    let gen03 = document.getElementById('gen03').value;
    if (!gen03) {
        gen03 = "3, 5"; // Default value
        document.getElementById('gen03').value = gen03; // Update the input field with default values
    }

    createSecondFrobeniusGraph();

}



function calculateSemigroup() {
    // Get the value from the input field
    const gen01 = document.getElementById('gen01').value;
    console.log(gen01)

    // Validate the input
    if (!isValidInput(gen01)) {
        alert("Please enter comma-separated integers only");
        return;
    }

    // Send data to the server using AJAX
    $.ajax({
        url: '/calculateSemigroup',
        method: 'POST',
        data: { gen01: gen01 },
        success: function(response) {
            if (response.error) {
            alert(response.error);
            return;
            }
            updateTable(response.result);
        }
    });
}


function updateTable(data) {
    // Create a string of numbers separated by commas
    const numbersString = data.join(", ");

    // Update the result div with the numbers string
    document.getElementById('result').innerText = numbersString;
}


function isValidInput(input) {
    // Regular expression to match integers separated by commas
    const regex = /^(\d+)(,\s*\d+)*$/;
    return regex.test(input);
}


function isValidSingleInteger(input) {
    // Regular expression to match a single integer
    const regex = /^\d+$/;
    return regex.test(input);
}


function calculateFactorizationLengths() {
    // Get the value from the input field
    const gen02 = document.getElementById('gen02').value;
    const element01 = document.getElementById('element01').value;

    // Validate the input
    if (!isValidInput(gen02)) {
        alert("Please enter comma-separated integers only");
        return;
    }

    // Validate the input
    if (!isValidSingleInteger(element01)) {
        alert("Please enter a single integer");
        return;
    }

    // Send data to the server using AJAX
    $.ajax({
        url: '/calculateFactorizationLengths',
        method: 'POST',
        data: { gen02: gen02, element01: element01 },
        success: function(response) {
            if (response.error) {
            alert(response.error);
            return;
            }
            // document.getElementById('result2').innerText = response.result2;
            // console.log('We are here')

            // Construct the table rows and cells
            let factorizationSet = response.result2[0].map(item => {
                return `(${item[0]}, ${item[1]})`;
            }).join(", ");
            
            let maxFactorizationLength = response.result2[1];
            let minFactorizationLength = response.result2[2];

            let tableRow = `
                <tr>
                    <td>${factorizationSet}</td>
                    <td>${maxFactorizationLength}</td>
                    <td>${minFactorizationLength}</td>
                </tr>
            `;

            // Insert the constructed row into the table's tbody
            document.querySelector('.table tbody').innerHTML = tableRow;

        }
    });

}


let myChartInstance;

function createSecondFrobeniusGraph() {
    // Get the value from the input field
    const gen03 = document.getElementById('gen03').value;

    // Validate the input
    if (!isValidInput(gen03)) {
        alert("Please enter comma-separated integers only");
        return;
    }

    $.ajax({
        url: '/createSecondFrobeniusGraph',
        method: 'POST',
        data: { gen03: gen03 },

        success: function(data) {
            
            const ctx = document.getElementById('myChart').getContext('2d');

            // If there's an existing chart instance, destroy it
            if (myChartInstance) {
                myChartInstance.destroy();
            }

            myChartInstance = new Chart(ctx, {
                type: 'line',
                data: data
            });
        },    


        error: function(error) {
            console.error("Error fetching data:", error);
        }
    });
}


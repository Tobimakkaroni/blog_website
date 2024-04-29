function calculateC4() {
    var inputc4 = parseInt(document.getElementById("inputc4").value);
    var gp = 0;
    var metal = 0;
    var sulf = 0;
    var granades = 0;
    var scrap = 0;
    var roundG = inputc4

    while (inputc4 > 0) {
        while (gp < 1000 || metal < 200 || sulf < 200) {
            gp += 18;
            metal += 25;
            granades++;

            while (sulf < 200 && gp > 1000) {
                gp -= 1;
                sulf += 1;
            }
        }
        gp -= 1000;
        metal -= 200;
        sulf -= 200;
        inputc4 -= 1;
        scrap = granades * 5;

        var result = "C4 produced! gp: " + gp + ", metal: " + metal + ", sulf: " + sulf + ", granades: " + (granades + roundG) + ", scrap: " + (scrap + (roundG * 5));
        document.getElementById("result").innerHTML += "<p>" + result + "</p>";
    }
}

function calculateRocket() {
    var inputRocket = parseInt(document.getElementById("inputRocket").value);
    var gp = 0;
    var metal = 0;
    var sulf = 0;
    var granades = 0;
    var scrap = 0;
    var roundG = inputRocket

    while (inputRocket > 0) {
        while (gp < 1000 || metal < 200 || sulf < 200) {
            gp += 18;
            metal += 25;
            granades++;

            while (sulf < 200 && gp > 1000) {
                gp -= 1;
                sulf += 1;
            }
        }
        gp -= 1000;
        metal -= 200;
        sulf -= 200;
        inputc4 -= 1;
        scrap = granades * 5;

        var result = "Rocket produced! gp: " + gp + ", metal: " + metal + ", sulf: " + sulf + ", granades: " + (granades + roundG) + ", scrap: " + (scrap + (roundG * 5));
        document.getElementById("resultRocket").innerHTML += "<p>" + result + "</p>";
    }
}
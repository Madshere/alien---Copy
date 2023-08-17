/* This function controls the breathing technique for the app. It utilizes the 'setInterval()' method to execute a callback at a given interval of time, thus making a transitory change on the HTML DOM.*/ 
function breathingTechnique() { 
    let breaths = 6; 
    let interval = setInterval(() => { 
        if (breaths > 0) { 
            document.getElementById('inhale').setAttribute('class', 'inhale active'); 
            document.getElementById('exhale').setAttribute('class', 'exhale inactive'); 
            breaths--; 
        } else if (breaths === 0) { 
            document.getElementById('inhale').setAttribute('class', 'inhale inactive'); 
            document.getElementById('exhale').setAttribute('class', 'exhale active'); 
        } 
    }, 2000); 
}

/* This function controls the grounding technique for the app. It utilizes the setTimeout() method to execute a callback after a certain period, thus making a persistent change on the HTML DOM.*/ 
function groundingTechnique() { 
    document.getElementById('grounding').setAttribute('class', 'grounding active'); 
    setTimeout(() => { 
        document.getElementById('grounding').setAttribute('class', 'grounding inactive'); 
    }, 60000); 
}
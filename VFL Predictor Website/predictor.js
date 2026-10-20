import * as benutils from "@benp2325/benutils";
import { rawCsvData } from "../Data/Sorted/sample-non-vfl/housing.js";

const csvData = rawCsvData.trim().split('\n').map(row=>row.split(','));

const feature_selection = {
    "TARGET":13,
    //put features below
    "CRIM":0,
    "ZN":1,
    "INDUS":2,
    "CHAS":3,
    "NOX":4,
    "RM":5,
    "AGE":6,
    "DIS":7,
    "RAD":8,
    "TAX":9,
    "PTRATIO":10,
    "B":11,
    "LSTAT":12
    }

//csv header safegaurd, default=0 or "no headers"
let start_index = 0;

//safegaurd for csv headers, just removing them because feature_selection handles labels
if(isNaN(parseFloat(csvData[0][feature_selection["TARGET"]]))){
    start_index = 1;
}


let model = window.trainedModel;

const observations = [];

const neuron_labels = [];

for(const feat_name of Object.keys(feature_selection)){
    if(feat_name != "TARGET"){
        neuron_labels.push(feat_name)
    }
}

for(let i = start_index; i<csvData.length; i++){
    const ob = {}
    for(const feat_name of Object.keys(feature_selection)){
        
        if(feat_name != "TARGET"){
            ob[feat_name] = parseFloat(csvData[i][feature_selection[feat_name]]);
            
        }
        
    }
    observations.push(ob);
};

const final_observations = [];

for(let i = 0; i<observations.length; i++){

    final_observations.push(model.predict(observations[i]));
}

window.finalObservations = final_observations;
window.neuronLabels = neuron_labels;

console.log(final_observations)

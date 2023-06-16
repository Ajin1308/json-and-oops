import json

indian_states = {
    'Karnataka': 'Bengaluru',
    'Maharashtra': 'Mumbai',
    'Tamil Nadu': 'Chennai',
    'Uttar Pradesh': 'Lucknow',
    'Rajasthan': 'Jaipur',
    'Gujarat': 'Gandhinagar',
    'West Bengal': 'Kolkata'
}

file =open('indian_states.json',"w")
json.dump(indian_states,file)
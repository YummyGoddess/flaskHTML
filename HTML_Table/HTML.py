from flask import Flask, render_template
app + Flask(__name__)

users = [
{ 'character_name' : 'Thor' ,'first_name' : 'Thor', 'last_name' : 'Odinson'},
{ 'character_name' : 'Iron-Main' ,'first_name' : 'Tony', 'last_name' : 'Stark'},
{ 'character_name' : 'Ant-Man' ,'first_name' : 'Henry', 'last_name' : 'Pym'},
{ 'character_name' : 'Hulk' ,'first_name' : 'Bruce', 'last_name' : 'Banner'},
{ 'character_name' : 'Captain-America' ,'first_name' : 'Steven', 'last_name' : 'Rogers'},
{ 'character_name' : 'Hawkeye' ,'first_name' : 'Clinton', 'last_name' : 'Barton'},
{ 'character_name' : 'Scarlet-Witch' ,'first_name' : 'Wanda', 'last_name' : 'Maximoff'},
{ 'character_name' : 'Black-Panter' ,'first_name' : "T'Challa", 'last_name' : 'Charles'},
{ 'character_name' : 'Black-Widow' ,'first_name' : 'Natalia', 'last_name' : 'Romanoff'},
{ 'character_name' : 'Mantis' ,'first_name' : 'Mandy', 'last_name' : 'Celestin'},
{ 'character_name' : 'Ms.Marvel' ,'first_name' : 'Carol', 'last_name' : 'Wilson'},
{ 'character_name' : 'Falcon' ,'first_name' : 'Samuel', 'last_name' : 'Wilson'},
{ 'character_name' : 'War-Machine' ,'first_name' : 'James', 'last_name' : 'Rhodes'},
{ 'character_name' : 'Spider-Man' ,'first_name' : 'Peter', 'last_name' : 'Parker'},
{ 'character_name' : 'Doctor-Strange' ,'first_name' : 'Stephen', 'last_name' : 'Strange'},
{ 'character_name' : 'Vison' ,'first_name' : 'Jonas', 'last_name' : 'None'},
]

@app.route('/')
def HTML(users):
    return render_template('index.html',users=users)







if__name__=="__main__":
app.run(debug=True)

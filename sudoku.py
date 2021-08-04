import os, uuid, generator, solveSudoku
from flask import Flask, render_template

gridSave = {}
guid = ""
app = Flask(__name__)

@app.route("/")
@app.route("/easy")
def home():
	grid = generator.doSolve(3)
	global gridSave
	global guid
	guid = uuid.uuid4().hex
	gridSave[guid] = grid
	#print(gridSave)
	return render_template('sudoku.html', grid=grid, guid=guid)
	
@app.route("/medium")
def medium():
	grid = generator.doSolve(6)
	global gridSave
	global guid
	guid = uuid.uuid4().hex
	gridSave[guid] = grid
	#print(gridSave)
	return render_template('sudoku.html', grid=grid, guid=guid)
	
@app.route("/hard")
def hard():
	grid = generator.doSolve(8)
	global gridSave
	global guid
	guid = uuid.uuid4().hex
	gridSave[guid] = grid
	#print(gridSave)
	return render_template('sudoku.html', grid=grid, guid=guid)
	
	
@app.route("/solve/<guid>")
def solve(guid=None):
	#grid_in = request.args.get('id')
	global gridSave
	#print(gridSave)
	grid = gridSave[guid]
	#print(grid)
	if solveSudoku.solveSudoku(grid) == True:
		#print("gridSave: ", gridSave)
		return render_template('sudoku.html', grid=grid, guid=guid)
	else:
		input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
		return render_template('sudoku.html', grid=input)
		

if __name__ == '__main__':
    app.run(debug=True)
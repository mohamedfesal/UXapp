
#=========================
# Import Flask Framwork
#=========================
from flask import Flask, render_template
app = Flask(__name__)

#=========================
# App Routes
#=========================

@app.route("/")
def home():
    return render_template("index.html", title="Home", companyName="UX Centers")

@app.route("/dashboard")
def bashboard():
    return render_template("/dashboard.html", title="Dashboard")

@app.route("/wfhsheet")
def wfhsheet():
    return render_template("/wfhsheet.html", title="WFH Sheet") 

@app.route("/returned")
def returned():
    return render_template("/returned.html", title="Returned PCs")
    
@app.route("/pcdetails")
def pcdetails():
    return render_template("/pcdetails.html", title="PCs Details")

@app.route("/stock")
def stock():
    return render_template("/stock.html", title="Stock")

@app.route("/stock/edit-stock-item")
def editStockItem():
    return render_template("/edit-stock-item.html", title="Edit Stock Item")
#=========================
# Run App
#=========================
if __name__ == "__main__":
    app.run(debug=True)

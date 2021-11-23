
#=========================
# Import Flask Framwork
#=========================
from flask import Flask, render_template
UXCentersApp = Flask(__name__)

#=========================
# App Routes
#=========================

@UXCentersApp.route("/")
def home():
    return render_template("index.html", title="Home", companyName="UX Centers")

@UXCentersApp.route("/dashboard")
def bashboard():
    return render_template("/dashboard.html", title="Dashboard")

@UXCentersApp.route("/wfhsheet")
def wfhsheet():
    return render_template("/wfhsheet.html", title="WFH Sheet") 

@UXCentersApp.route("/returned")
def returned():
    return render_template("/returned.html", title="Returned PCs")
    
@UXCentersApp.route("/pcdetails")
def pcdetails():
    return render_template("/pcdetails.html", title="PCs Details")

@UXCentersApp.route("/stock")
def stock():
    return render_template("/stock.html", title="Stock")

@UXCentersApp.route("/stock/edit-stock-item")
def editStockItem():
    return render_template("/edit-stock-item.html", title="Edit Stock Item")
#=========================
# Run App
#=========================
if __name__ == "__main__":
    UXCentersApp.run(debug=True)

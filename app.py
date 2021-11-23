
#=========================
# Import Flask Framwork
#=========================
from flask import Flask, render_template
UxApp = Flask(__name__)

#=========================
# App Routes
#=========================

@UxApp.route("/")
def home():
    return render_template("index.html", title="Home", companyName="UX Centers")

@UxApp.route("/dashboard")
def bashboard():
    return render_template("/dashboard.html", title="Dashboard")

@UxApp.route("/wfhsheet")
def wfhsheet():
    return render_template("/wfhsheet.html", title="WFH Sheet") 

@UxApp.route("/returned")
def returned():
    return render_template("/returned.html", title="Returned PCs")
    
@UxApp.route("/pcdetails")
def pcdetails():
    return render_template("/pcdetails.html", title="PCs Details")

@UxApp.route("/stock")
def stock():
    return render_template("/stock.html", title="Stock")

@UxApp.route("/stock/edit-stock-item")
def editStockItem():
    return render_template("/edit-stock-item.html", title="Edit Stock Item")
#=========================
# Run App
#=========================
if __name__ == "__main__":
    UxApp.run(host='127.0.0.1', port=8080, debug=True)
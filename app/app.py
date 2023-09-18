from flask import Flask, render_template, request
from backend import ip_validation, calculate_subnet, get_subnet_from_cidr, get_cidr_from_subnets, get_cidr_from_hosts

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ip = ""
    ip_class = ""
    cidr = ""
    subnet_mask = ""
    subnets = ""
    error = ""

    if request.method == "POST":
        ip = request.form["ip"]
        choice = request.form["choice"]

        valid, ip_class = ip_validation(ip)

        if not valid:
            error = "Invalid IP Address! Please enter valid IP xxx.xxx.xxx.xxx"
        else:
            if choice == "1":
                cidr = request.form["cidr"]
                if not (0 <= int(cidr) <= 32):
                    error = "Invalid CIDR !"
                else:
                    subnets, subnet_mask = calculate_subnet(ip_class, cidr)
            elif choice == "2":
                num_hosts = int(request.form["num_hosts"])
                cidr = get_cidr_from_hosts(num_hosts)
                subnets, subnet_mask = calculate_subnet(ip_class, cidr)
            elif choice == "3":
                num_subnets = int(request.form["num_subnets"])
                cidr = get_cidr_from_subnets(num_subnets)
                subnets, subnet_mask = calculate_subnet(ip_class, cidr)
            else:
                error = "Invalid choice!"

    return render_template("index.html", ip=ip, ip_class=ip_class, subnet_mask=subnet_mask, subnets=subnets, error=error)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

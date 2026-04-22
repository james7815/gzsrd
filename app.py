from flask import Flask, render_template

app = Flask(__name__)

# 首页
@app.route('/')
def index():
    return render_template('index.html', title='首页')

# 关于我们
@app.route('/about')
def about():
    return render_template('about.html', title='关于我们')

# 产品中心
@app.route('/products')
def products():
    # 模拟产品数据，实际开发中通常来自数据库
    product_list = [
        {"name": "高速PCB电路板", "desc": "多层精密线路板，适用于工业控制"},
        {"name": "嵌入式核心模块", "desc": "ARM架构低功耗主控板"},
        {"name": "智能传感器套件", "desc": "工业级物联网数据采集单元"}
    ]
    return render_template('products.html', title='产品中心', products=product_list)

# 联系我们
@app.route('/contact')
def contact():
    return render_template('contact.html', title='联系我们')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
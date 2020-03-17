from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Grid
import pandas as pd

# 设置保留百分比位数
keep_point = 2

df = pd.read_csv('some-data.csv')
datal1 = df['data1']
datal2 = df['data2']
xlist = df['name']
percent = datal1 / datal2

x_ox = [x for x in xlist]

c = (
    Bar()
        .add_xaxis(x_ox)
        .add_yaxis("实际耗费", [x for x in datal1])
        .add_yaxis("计划耗费", [x for x in datal2])
        .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value}%"), interval=5
        )
    )
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45,font_size=20)),
        title_opts=opts.TitleOpts(title="Bar-读csv并有两个方向缩放", subtitle="解决标签名字过长的问题"),
        # datazoom_opts=[opts.DataZoomOpts()],#,opts.DataZoomOpts(orient="vertical")],
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True),

    )
)

line = (
    Line()
        .add_xaxis(x_ox)
        .add_yaxis('计算占比', [round(x, keep_point) for x in percent * 100],
                   yaxis_index=1,
                   linestyle_opts=opts.LineStyleOpts(color="#209AC9"),
                   itemstyle_opts=opts.ItemStyleOpts(border_color="#209AC9", border_width=3),
                   label_opts=opts.LabelOpts(font_size=20, color='#209AC9', is_show=True), symbol_size=14)
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-连接空数据"))
)

#这个视二合一用的
overlap = c.overlap(line)

#这个是渲染用的
grid = (
    Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
        .add(
        overlap, grid_opts=opts.GridOpts(), is_control_axis_index=True
    )
        .render("grid_overlap_multi_xy_axis.html")
)

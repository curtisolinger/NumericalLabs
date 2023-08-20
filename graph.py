from random import randint, random
import pandas as pd

# print(randint(10, 100))
# print(random() * 10)

def create_dataframe:
    x_values = []
    for i in range(100):
        x_values.append(i + 1)

    y_values = []
    for i in range(100):
        y_values.append(random() * 10)

    data = [x_values, y_values]
    df = pd.DataFrame(list(zip(x_values, y_values)), columns = ["x_values", "y_values"])
    return(df)


def create_chart():

    df = create_dataframe()

    chart = {
      "$schema": "https://vega.github.io/schema/vega/v5.json",
      "width": 400,
      "height": 200,
      "padding": 5,

      "data": [
        {
          "name": "table",
          "source": df
        }
      ],

      "signals": [
        {
          "name": "tooltip",
          "value": {},
          "on": [
            {"events": "rect:mouseover", "update": "datum"},
            {"events": "rect:mouseout",  "update": "{}"}
          ]
        }
      ],

      "scales": [
        {
          "name": "xscale",
          "type": "linear",
          "domain": {"data": "table", "field": "x_values"},
          "range": "width",
          "padding": 0.05,
          "round": true
        },
        {
          "name": "yscale",
          "domain": {"data": "table", "field": "y_values"},
          "nice": true,
          "range": "height"
        }
      ],

      "axes": [
        { "orient": "bottom", "scale": "xscale" },
        { "orient": "left", "scale": "yscale" }
      ],

      "marks": [
        {
          "type": "rect",
          "from": {"data":"table"},
          "encode": {
            "enter": {
              "x": {"scale": "xscale", "field": "category"},
              "width": {"scale": "xscale", "band": 1},
              "y": {"scale": "yscale", "field": "amount"},
              "y2": {"scale": "yscale", "value": 0}
            },
            "update": {
              "fill": {"value": "steelblue"}
            },
            "hover": {
              "fill": {"value": "red"}
            }
          }
        },
        {
          "type": "text",
          "encode": {
            "enter": {
              "align": {"value": "center"},
              "baseline": {"value": "bottom"},
              "fill": {"value": "#333"}
            },
            "update": {
              "x": {"scale": "xscale", "signal": "tooltip.category", "band": 0.5},
              "y": {"scale": "yscale", "signal": "tooltip.amount", "offset": -2},
              "text": {"signal": "tooltip.amount"},
              "fillOpacity": [
                {"test": "isNaN(tooltip.amount)", "value": 0},
                {"value": 1}
              ]
            }
          }
        }
      ]
    }
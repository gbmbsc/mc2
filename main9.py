import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

################################################################################
# LENZING TABLE
################################################################################

lenzing_row_labels = [
    "LAG",
    "Δ since 1 month",
    "Δ since 1 year",
    "budget*",
]

lenzing_data = [
    [  # Row 1 (LAG)
        "970",         # Spot Hardwood
        "1080",        # Spot Softwood
        "110",         # Spread SW-HW
        "13800",       # VSF Medium
        "13800",       # VSF High
        "12940",       # Lyocell (CN)
        "57,5%",       # Spread in %
        "13920",       # Cotton #1 Spot
        "13890",       # Jän.25
        "14090",       # Nov.25
        "0,71",        # Cotton #2 Spot
        "0,71",        # Mär.25
        "0,73",        # Mär.26
    ],
    [  # Row 2 (Δ since 1 month)
        "0,2%",
        "0,0%",
        "-1,8%",
        "-0,1%",
        "0,1%",
        "-0,1%",
        "1,3%",
        "-0,2%",
        "",
        "",
        "2,0%",
        "",
        "",
    ],
    [  # Row 3 (Δ since 1 year)
        "7,8%",
        "18,7%",
        "1000.0%",
        "7,3%",
        "5,7%",
        "-5,1%",
        "3,4%",
        "-7,3%",
        "",
        "",
        "-10,9%",
        "",
        "",
    ],
    [  # Row 4 (budget*)
        "9,0%",
        "",
        "633,3%",
        "",
        "-3,2%",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ],
]

def make_lenzing_table_white_borders():
    """
    Creates the LENZING table:
      - 3 header rows 
      - 4 data rows
      - White borders, row-grey, budget* color-coded cells
    """
    # Table-level style
    table_style = {
        "borderCollapse": "collapse",
        "borderSpacing": "0",
        "border": "1px solid #fff",  # White borders
        "margin": "0px",
        "padding": "0px",
        "fontSize": "10px",
        "width": "80%",
    }

    # Row1 (green header)
    row1_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#82D535",  # Lenzing-Grün
        "color": "black",
        "minWidth": "240px",
    }

    row1_th_style_3col = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#82D535",  # Lenzing-Grün
        "color": "black",
        "minWidth": "80px",
    }

    row1_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#82D535",  # Lenzing-Grün
        "color": "black",
        "minWidth": "120px",
        #"maxWidth": "10px",
    }

    row1 = html.Tr(
        [
            html.Th("", style=row1_th_style_1st),  # blank cell
            html.Th("Dissolving Wood Pulp²", colSpan=3, style=row1_th_style_3col),
            html.Th("Viscose Staple Fibre", colSpan=3, style=row1_th_style_3col),
            html.Th("Spread DWP / VSF", colSpan=3, style=row1_th_style),
            html.Th("Cotton #1 (ZCE)", colSpan=3, style=row1_th_style_3col),
            html.Th("Cotton #2 (ICE) 1)", colSpan=3, style=row1_th_style_3col),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Row2 (grey header)

    row2_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "minWidth": "80px",
    }

    row2_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "maxWidth": "80px",
    }
    row2 = html.Tr(
        [
            html.Th("", style=row2_th_style_1st),
            html.Th("USD to", colSpan=3, style=row2_th_style),
            html.Th("CNY to", colSpan=3, style=row2_th_style),
            html.Th("in %", colSpan=3, style=row2_th_style),
            html.Th("CNY/MT", colSpan=3, style=row2_th_style),
            html.Th("USD / Ib", colSpan=3, style=row2_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Row3 (grey header)
    row3_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "width": "80px",
    }
    row3 = html.Tr(
        [
            html.Th("", style=row3_th_style),
            html.Th("Spot Hardwood", style=row3_th_style),
            html.Th("Spot Softwood", style=row3_th_style),
            html.Th("Spread SW-HW", style=row3_th_style),
            html.Th("VSF Medium", style=row3_th_style),
            html.Th("VSF High", style=row3_th_style),
            html.Th("Lyocell (CN)", style=row3_th_style),
            html.Th("DWP Hardwood / VSF High", colSpan=3, style=row3_th_style),
            html.Th("Spot", style=row3_th_style),
            html.Th("Jän.25", style=row3_th_style),
            html.Th("Nov.25", style=row3_th_style),
            html.Th("Spot", style=row3_th_style),
            html.Th("Mär.25", style=row3_th_style),
            html.Th("Mär.26", style=row3_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Data rows
    td_style_base = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#F2F4F1",
        "color": "black",
        "minWidth": "80px",
    }
    td_style_row_header = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "left",
        "backgroundColor": "#ffffff",
        "color": "black",
    }

    data_trs = []
    for i, label in enumerate(lenzing_row_labels):
        row_cells = []
        # Leftmost cell (row label):
        row_cells.append(html.Td(label, style=td_style_row_header))

        for j, val in enumerate(lenzing_data[i]):
            cell_style = td_style_base.copy()
            # Example background color logic:
            if i == 3 and isinstance(val, str) and val.strip().endswith("%"):
                if val.strip().startswith("-"):
                    cell_style["backgroundColor"] = "#FF5865"  # negative => red
                else:
                    cell_style["backgroundColor"] = "#7EFF45"  # positive => green

            # Give the 8th column a colSpan of 3
            if j == 7:  # j=7 is the 8th column (0-based)
                row_cells.append(
                    html.Td(val, style=cell_style, colSpan=3)
                )
            else:
                row_cells.append(html.Td(val, style=cell_style))

        data_trs.append(html.Tr(row_cells, style={"margin": "0px", "padding": "0px"}))
    """
    data_trs = []
    for i, label in enumerate(lenzing_row_labels):
        row_cells = []
        # Leftmost cell (row label):
        row_cells.append(html.Td(label, style=td_style_row_header))
        # Subsequent cells
        for val in lenzing_data[i]:
            cell_style = td_style_base.copy()
            # If "budget*" row (i == 3) and cell ends with "%"
            if i == 3 and isinstance(val, str) and val.strip().endswith("%"):
                if val.strip().startswith("-"):
                    cell_style["backgroundColor"] = "#FF5865"  # negative => red
                else:
                    cell_style["backgroundColor"] = "#7EFF45"  # positive => green
            row_cells.append(html.Td(val, style=cell_style))

        data_trs.append(html.Tr(row_cells, style={"margin": "0px", "padding": "0px"}))
    """
    # Assemble the table
    return html.Table(
        [row1, row2, row3] + data_trs,
        style=table_style,
    )




################################################################################
# SEMPERIT TABLE
################################################################################

semperit_row_labels = [
    "LAG",
    "Δ since 1 month",
    "Δ since 1 year",
    "budget*",
]

semperit_data = [
    [  # Row 1 (LAG)
        "205,50",         # Spot Hardwood
        "0,00",        # Spot Softwood
        "211,70",         # Spread SW-HW
        "960",       # VSF Medium
        "",       # VSF High
        "1060",       # Lyocell (CN)
        "102,44",       # Spread in %
        "480,25",       # Cotton #1 Spot
        #"13890",       # Jän.25
        #"",       # Nov.25
        #"",        # Cotton #2 Spot
        #"",        # Mär.25
        #" ",        # Mär.26
    ],
    [  # Row 2 (Δ since 1 month)
        "3,0%",
        "",
        "",
        "-13,5%",
        "",
        "-22,9%",
        "-2,5%",
        "-4,7%",
        #"",
        #"",
        #"2,0%",
        #"",
        #"",
    ],
    [  # Row 3 (Δ since 1 year)
        "44,5%", #1
        "", #2
        "", #3
        "37,1%", #4
        "", #5
        "11,6%", #6
        "-23,8%", #7
        "6,9%", #8
        #"",
        #"",
        #"-10,9%",
        #"",
        #"",
    ],
    [  # Row 4 (budget*)
        "42,1%", #1
        "", #2
        "17,5%", #3
        "", #4
        "", #5
        "", #6
        "", #7
        "", #8
        #"", #9
        #"", #10
        #"", #11
        #"", #12
        #"", 
    ],
]

def make_semperit_table_white_borders():

    # Table-level style
    table_style = {
        "borderCollapse": "collapse",
        "borderSpacing": "0",
        "border": "1px solid #fff",  # White borders
        "margin": "0px",
        "padding": "0px",
        "fontSize": "10px",
        "width": "80%",
    }

    # Row1 (green header)
    row1_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#203F65",  # Semperit Blue
        "color": "white",
        "minWidth": "240px",
    }

    row1_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#203F65",  # Semperit Blue
        "color": "white",
        "width": "120px",
    }

    row1 = html.Tr(
        [
            html.Th("", style=row1_th_style_1st),
            html.Th("Rubber TSR 20 1)", colSpan=3, style=row1_th_style),
            html.Th("Butadiene 3)", colSpan=3, style=row1_th_style),
            html.Th("Iron Ore 62% (incl Cost & Freight) 3)", colSpan=3, style=row1_th_style),
            html.Th("Coaltar 3)", colSpan=3, style=row1_th_style),
            html.Th("", colSpan=3, style=row1_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Row2 (grey header)
    row2_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "white",
        "minWidth": "120px",
    }

    row2_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "maxWidth": "80px",
    }
    
    row2 = html.Tr(
        [
            html.Th("", style=row2_th_style_1st),
            html.Th("USD to", colSpan=3, style=row2_th_style),
            html.Th("CNY to", colSpan=3, style=row2_th_style),
            html.Th("in %", colSpan=3, style=row2_th_style),
            html.Th("CNY/MT", colSpan=3, style=row2_th_style),
            html.Th("", colSpan=3, style=row2_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Row3 (grey header)
    row3_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "minWidth": "80px",
    }
    
    row3_th_style_3col = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "minWidth": "240px",
    }

    row3 = html.Tr(
        [
            html.Th("", style=row3_th_style),
            html.Th("Spot", style=row3_th_style),
            html.Th("Jän.25", style=row3_th_style),
            html.Th("Dez.26", style=row3_th_style),
            html.Th("Spot EU", style=row3_th_style),
            html.Th("", style=row3_th_style),
            html.Th("Spot Korea", style=row3_th_style),
            html.Th("China", colSpan=3, style=row3_th_style),
            html.Th("HFO 1% NW Europe", colSpan=3, style=row3_th_style_3col),
            #html.Th("Jän.25", style=row3_th_style),
            #html.Th("Nov.25", style=row3_th_style),
            html.Th("", style=row3_th_style),
            html.Th("", style=row3_th_style),
            html.Th("", style=row3_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Data rows
    td_style_base = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#F2F4F1",
        "color": "black",
        "minWidth": "80px",
    }
    td_style_row_header = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "left",
        "backgroundColor": "#ffffff",
        "color": "black",
    }

    data_trs = []
    for i, label in enumerate(semperit_row_labels):
        row_cells = []
        # Leftmost cell (row label):
        row_cells.append(html.Td(label, style=td_style_row_header))

        for j, val in enumerate(semperit_data[i]):
            cell_style = td_style_base.copy()
            # Example background color logic:
            if i == 3 and isinstance(val, str) and val.strip().endswith("%"):
                if val.strip().startswith("-"):
                    cell_style["backgroundColor"] = "#7EFF45"  # negative => red
                else:
                    cell_style["backgroundColor"] = "#FF5865"  # positive => green

            # Give the 8th column a colSpan of 3
            if j == 6:  # j=7 is the 8th column (0-based)
                row_cells.append(
                    html.Td(val, style=cell_style, colSpan=3)
                )
            #elif j == 4:  # j=7 is the 8th column (0-based)
            #    row_cells.append(
            #        html.Td(val, style=cell_style, colSpan=3)
            #    )
            else:
                row_cells.append(html.Td(val, style=cell_style))

        data_trs.append(html.Tr(row_cells, style={"margin": "0px", "padding": "0px"}))
    

    """
    data_trs = []
    for i, label in enumerate(semperit_row_labels):
        row_cells = []
        # Leftmost cell (row label):
        row_cells.append(html.Td(label, style=td_style_row_header))
        # Subsequent cells
        for val in semperit_data[i]:
            cell_style = td_style_base.copy()
            # If "budget*" row (i == 3) and cell ends with "%"
            if i == 3 and isinstance(val, str) and val.strip().endswith("%"):
                if val.strip().startswith("-"):
                    cell_style["backgroundColor"] = "#7EFF45"  # negative => gree
                else:
                    cell_style["backgroundColor"] = "#FF5865"  # positive => red
            row_cells.append(html.Td(val, style=cell_style))

        data_trs.append(html.Tr(row_cells, style={"margin": "0px", "padding": "0px"}))
    """

    # Assemble the table
    return html.Table(
        [row1, row2, row3] + data_trs,
        style=table_style,
    )





################################################################################
# AMAG TABLE
################################################################################

amag_row_labels = [
    "2024-12-06",
    "Δ since 1 month",
    "Δ since 1 year",
    "Δ budget*",
]

amag_data = [
    [  # Row 1 (LAG)
        "2683",         # Spot Hardwood
        "2629",        # Spot Softwood
        "2678",         # Spread SW-HW
        "803",       # VSF Medium
        "30,6%",       # VSF High
        "468,98",       # Lyocell (CN)
        "",       # Spread in %
        "360,50",       # Cotton #1 Spot
        "1834",       # Jän.25
        "1849",       # Nov.25
        "1849",        # Cotton #2 Spot
        #"",        # Mär.25
        #" ",        # Mär.26
    ],
    [  # Row 2 (Δ since 1 month)
        "1,2%",
        "1,2%",
        "-2,1%",
        "11,7%",
        "10,4%",
        "0,0%",
        "",
        "8,3%",
        "-8,3%",
        "",
        "",
        #"",
        #"",
    ],
    [  # Row 3 (Δ since 1 year)
        "17,7%", #1
        "23,3%", #2
        "17,7%", #3
        "141,2%", #4
        "95,6%", #5
        "5,0%", #6
        "", #7
        "67,3%", #8
        "-29,0%",
        "",
        "",
        #"",
        #"",
    ],
    [  # Row 4 (budget*)
        "22,0%", #1
        "19,5%", #2
        "", #3
        "136,3%", #4
        "", #5
        "4,2%", #6
        "", #7
        "", #8
        "", #9
        "", #10
        "", #11
        #"", #12
        #"", 
    ],
]



def make_amag_table_white_borders():

    # Table-level style
    table_style = {
        "borderCollapse": "collapse",
        "borderSpacing": "0",
        "border": "1px solid #fff",  # White borders
        "margin": "0px",
        "padding": "0px",
        "fontSize": "10px",
        "width": "80%",
    }

    # Row1 (green header)
    row1_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#8DB4E2",  # AMAG Blue
        "color": "black",
        #"width": "240px",
        "minWidth": "240px",
    }

    row1_th_style_3col = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#8DB4E2",  # AMAG Blue
        "color": "black",
        "width": "80px",
    }


    row1_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#8DB4E2",  # AMAG Blue
        "color": "black",
        "width": "120px",
    }

    row1 = html.Tr(
        [
            html.Th("", style=row1_th_style_1st),
            html.Th("Aluminium (LME) 1)", colSpan=3, style=row1_th_style),
            html.Th("Alumina - Tonerde (API) 9)", colSpan=3, style=row1_th_style),
            html.Th("Verhältnis Tonerde/ Alum (API/3M-LME)", colSpan=3, style=row1_th_style),
            html.Th("3M-LME Premium 4)", colSpan=3, style=row1_th_style),
            html.Th("Coke (DCE) 1)", colSpan=3, style=row1_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Row2 (grey header)
    row2_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "white",
        "minWidth": "120px",
    }

    row2_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "maxWidth": "80px",
    }
    
    row2 = html.Tr(
        [
            html.Th("", style=row2_th_style_1st),
            html.Th("USD / to", colSpan=3, style=row2_th_style),
            html.Th("USD / to", colSpan=3, style=row2_th_style),
            html.Th("%", colSpan=3, style=row2_th_style),
            html.Th("USD / to", colSpan=3, style=row2_th_style),
            html.Th("CNY / MT", colSpan=3, style=row2_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Row3 (grey header)
    row3_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "width": "80px",
    }

    row3 = html.Tr(
        [
            html.Th("Date", style=row3_th_style),
            html.Th("Sport", style=row3_th_style),
            html.Th("3M-LME", style=row3_th_style),
            html.Th("Dez.25", style=row3_th_style),
            html.Th("Spot", colSpan=3, style=row3_th_style),
            html.Th("API / 3M-LME", colSpan=3, style=row3_th_style),
            html.Th("US MidWest", style=row3_th_style),
            html.Th("", style=row3_th_style),
            html.Th("Rotterdam", style=row3_th_style),
            html.Th("Spot", style=row3_th_style),
            html.Th("3M", style=row3_th_style),
            html.Th("12M", style=row3_th_style),
            #html.Th("", style=row3_th_style),
            #html.Th("", style=row3_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Data rows
    td_style_base = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#F2F4F1",
        "color": "black",
        "minWidth": "40px",
        "maxWidth": "120px",
    }
    td_style_row_header = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "left",
        "backgroundColor": "#ffffff",
        "color": "black",
    }

    data_trs = []
    for i, label in enumerate(amag_row_labels):
        row_cells = []
        # Leftmost cell (row label):
        row_cells.append(html.Td(label, style=td_style_row_header))

        for j, val in enumerate(amag_data[i]):
            cell_style = td_style_base.copy()
            # Example background color logic:
            if i == 3 and (j < 3 or j > 4) and isinstance(val, str) and val.strip().endswith("%"):
                if val.strip().startswith("-"):
                    cell_style["backgroundColor"] = "#FF5865"  # negative => red
                else:
                    cell_style["backgroundColor"] = "#7EFF45"  # positive => green
                    
            elif i == 3 and j > 2 and  isinstance(val, str) and val.strip().endswith("%"):
                if val.strip().startswith("-"):
                    cell_style["backgroundColor"] = "#7EFF45"  # negative => red
                else:
                    cell_style["backgroundColor"] = "#FF5865"  # positive => green
                    
            #else:
            #    if val.strip().startswith("+"):
                    #cell_style["backgroundColor"] = "#7EFF45"  # negative => red
            #    else:
                    #cell_style["backgroundColor"] = "#FF5865"  # positive => green

            # Give the 8th column a colSpan of 3
            if j == 3:  # j=7 is the 8th column (0-based)
                row_cells.append(
                    html.Td(val, style=cell_style, colSpan=3)
                )
            elif j == 4:  # j=7 is the 8th column (0-based)
                row_cells.append(
                    html.Td(val, style=cell_style, colSpan=3)
                )
            else:
                row_cells.append(html.Td(val, style=cell_style))

        data_trs.append(html.Tr(row_cells, style={"margin": "0px", "padding": "0px"}))
    
    """
    data_trs = []
    for i, label in enumerate(amag_row_labels):
        row_cells = []
        # Leftmost cell (row label):
        row_cells.append(html.Td(label, style=td_style_row_header))
        # Subsequent cells
        for val in amag_data[i]:
            cell_style = td_style_base.copy()
            # If "budget*" row (i == 3) and cell ends with "%"
            if i == 3 and isinstance(val, str) and val.strip().endswith("%"):
                if val.strip().startswith("-"):
                    cell_style["backgroundColor"] = "#orange"  # negative => green
                else:
                    cell_style["backgroundColor"] = "orange"  # positive => red
            row_cells.append(html.Td(val, style=cell_style))

        data_trs.append(html.Tr(row_cells, style={"margin": "0px", "padding": "0px"}))
    """

    # Assemble the table
    return html.Table(
        [row1, row2, row3] + data_trs,
        style=table_style,
    )




################################################################################
# ENERGY TABLE
################################################################################

energy_row_labels = [
    "2024-12-06",
    "Δ since 1 month",
    "Δ since 1 year",
    #"Δ budget*",
]

energy_data = [
    [  # Row 1 (LAG)
        "72,09",         # Spot Hardwood
        "71,68",        # Spot Softwood
        "70,00",         # Spread SW-HW
        "46,55",       # VSF Medium
        "46,34",       # VSF High
        "41,64",       # Lyocell (CN)
        "128,33",       # Spread in %
        "2256,46",       # Cotton #1 Spot
        "1160",       # Jän.25
        #"1849",       # Nov.25
        #"1849",        # Cotton #2 Spot
        #"",        # Mär.25
        #" ",        # Mär.26
    ],
    [  # Row 2 (Δ since 1 month)
        "-3,8%",
        "",
        "",
        "15,3%",
        "",
        "",
        "10,6%",
        "k.A.",
        "-20,1%",
        #"",
        #"",
        #"",
        #"",
    ],
    [  # Row 3 (Δ since 1 year)
        "-3,0%", #1
        "", #2
        "", #3
        "18,4%", #4
        "", #5
        "", #6
        "9,7%", #7
        "k.A.", #8
        "-59,3%",
        #"",
        #"",
        #"",
        #"",
    ],

]


def make_energy_table_white_borders():

    # Table-level style
    table_style = {
        "borderCollapse": "collapse",
        "borderSpacing": "0",
        "border": "1px solid #fff",  # White borders
        "margin": "0px",
        "padding": "0px",
        "fontSize": "10px",
        "width": "80%",
    }

    # Row1 (green header)
    row1_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#C4BD97",  # Energy Gold
        "color": "black",
        "width": "240px",
    }

    row1_th_style_3col = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#C4BD97",  # Energy Gold
        "color": "black",
        "minWidth": "240px",
    }

    row1_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#C4BD97",  # Energy Gold
        "color": "black",
        "width": "120px",
    }

    row1 = html.Tr(
        [
            html.Th("", style=row1_th_style_1st),
            html.Th("Crude Oil Brent (ICE) 1)", colSpan=3, style=row1_th_style_3col),
            html.Th("Natural Gas - TTF (ICE) 1)", colSpan=3, style=row1_th_style_3col),
            html.Th("Electricity Phelix Baseload (EEX) 7)", colSpan=3, style=row1_th_style_3col),
            html.Th("Shanghai Container Freight Index 5)", colSpan=3, style=row1_th_style_3col),
            html.Th("BDI Baltic Exchange Dry Index 6)", colSpan=3, style=row1_th_style_3col),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Row2 (grey header)

    row2_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "white",
        "minWidth": "120px",
    }

    row2_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "maxWidth": "80px",
    }
    
    row2 = html.Tr(
        [
            html.Th("", style=row2_th_style_1st),
            html.Th("USD / bbl", colSpan=3, style=row2_th_style),
            html.Th("EUR / MWh", colSpan=3, style=row2_th_style),
            html.Th("EUR / MWh", colSpan=3, style=row2_th_style),
            html.Th("USD/TEU (20ft) Shanghai-Europe", colSpan=3, style=row2_th_style),
            html.Th("Index in Punkten", colSpan=3, style=row2_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Row3 (grey header)
    row3_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",
        "color": "black",
        "width": "80px",
    }

    row3 = html.Tr(
        [
            html.Th("Date", style=row3_th_style),
            html.Th("Spot", style=row3_th_style),
            html.Th("3M", style=row3_th_style),
            html.Th("12M", style=row3_th_style),
            html.Th("Spot", style=row3_th_style),
            html.Th("3M", style=row3_th_style),
            html.Th("12M", style=row3_th_style),
            html.Th("Spot", colSpan=3, style=row3_th_style),
            html.Th("Spot", colSpan=3, style=row3_th_style),
            html.Th("Spot", colSpan=3, style=row3_th_style),
            #html.Th("3M", style=row3_th_style),
            #html.Th("12M", style=row3_th_style),
            #html.Th("", style=row3_th_style),
            #html.Th("", style=row3_th_style),
        ],
        style={"margin": "0px", "padding": "0px"},
    )

    # Data rows
    td_style_base = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#F2F4F1", # #F2F4F1
        "color": "black",
        "minWidth": "80px",
    }
    td_style_row_header = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "left",
        "backgroundColor": "#ffffff",
        "color": "black",
    }

    """
    data_trs = []
    for i, label in enumerate(energy_row_labels):
        row_cells = []
        # Leftmost cell (row label):
        row_cells.append(html.Td(label, style=td_style_row_header))
        # Subsequent cells
        for val in energy_data[i]:
            cell_style = td_style_base.copy()
            # If "budget*" row (i == 3) and cell ends with "%"
            #if i == 3 and isinstance(val, str) and val.strip().endswith("%"):
            #    if val.strip().startswith("-"):
            #        cell_style["backgroundColor"] = "#orange"  # negative => green
            #    else:
            #        cell_style["backgroundColor"] = "orange"  # positive => red
            row_cells.append(html.Td(val, style=cell_style))

        data_trs.append(html.Tr(row_cells, style={"margin": "0px", "padding": "0px"}))
    """

    data_trs = []
    for i, label in enumerate(energy_row_labels):
        row_cells = []
        # Leftmost cell (row label):
        row_cells.append(html.Td(label, style=td_style_row_header))

        for j, val in enumerate(energy_data[i]):
            cell_style = td_style_base.copy()
            # Example background color logic:
            #if i == 3 and isinstance(val, str) and val.strip().endswith("%"):
            #    if val.strip().startswith("-"):
            #        cell_style["backgroundColor"] = "#FF5865"  # negative => red
            #    else:
            #        cell_style["backgroundColor"] = "#7EFF45"  # positive => green

            # Give the 8th column a colSpan of 3
            if j == 6:  # j=7 is the 8th column (0-based)
                row_cells.append(
                    html.Td(val, style=cell_style, colSpan=3)
                )
            elif j == 7:  # j=7 is the 8th column (0-based)
                row_cells.append(
                    html.Td(val, style=cell_style, colSpan=3)
                )
            elif j == 8:  # j=7 is the 8th column (0-based)
                row_cells.append(
                    html.Td(val, style=cell_style, colSpan=3)
                )
            else:
                row_cells.append(html.Td(val, style=cell_style))

        data_trs.append(html.Tr(row_cells, style={"margin": "0px", "padding": "0px"}))



    # Assemble the table
    return html.Table(
        [row1, row2, row3] + data_trs,
        style=table_style,
    )











################################################################################
# STOCK Market
################################################################################

stockmarket_row_labels = [
    "2024-12-05",
    "Δ since 1 day",
    "Δ since 1 month",
    "Δ since 1 year",
    "52w high",
    "52w low",
    "YTD",
    #"Δ budget*",
]

stockmarket_data = [
    [  # Row 1 (LAG)
        "3574,83",         # Spot Hardwood
        "1781,74",        # Spot Softwood
        "44765,71",         # Spread SW-HW
        "4951,58",       # VSF Medium
        "20358,80",       # VSF High
        "3368,86",       # Lyocell (CN)
        "30,95",       # Spread in %
        "11,68",       # Cotton #1 Spot
        "24,40",       # Jän.25
        #"1",       # Nov.25
        #"2",        # Cotton #2 Spot
        #"3",        # Mär.25
        #"4",        # Mär.26
    ],

    [  # Row 2 (Δ since 1 day)
        "0,95%",
        "0,89%",
        "-0,55%",
        "0,66%",
        "0,78%",
        "1,18%",
        "2,47%",
        "-0,34%",
        "0,00%",
        #"",
        #"",
        #"",
        #"",
    ],

    [  # Row 3 (Δ since 1 month)
        "1,74%",
        "1,67%",
        "2,37%",
        "3,14%",
        "7,09%",
        "0,61%",
        "-1,11%",
        "2,63%",
        "-0,81%",
        #"",
        #"",
        #"",
        #"",
    ],

    [  # Row 3 (Δ since 1 year)
        "8,18%",
        "7,62%",
        "24,16%",
        "10,45%",
        "22,41%",
        "14,67%",
        "-7,57%",
        "-16,55%",
        "-9,63%",
        #"",
        #"",
        #"",
        #"",
    ],

    [  # Row 4 (52w high)
        "3775,49",
        "1887,05",
        "45014,04",
        "5100,90",
        "20358,80",
        "3489,78",
        "37,30",
        "15,56",
        "31,10",
        #"",
        #"",
        #"",
        #"",
    ],

    [  # Row 5 (52w low)
        "3290,19",
        "1649,64",
        "36054,43",
        "4303,08",
        "16431,49",
        "2702,19",
        "24,85",
        "10,24",
        "22,30",
        #"",
        #"",
        #"",
        #"",
    ],

    [  # Row 6 (YTD)
        "4,14%",
        "3,48%",
        "18,77%",
        "9,51%",
        "21,71%",
        "14,44%",
        "-12,38%",
        "-17,37%",
        "-8,61%",
        #"",
        #"",
        #"",
        #"",
    ],

]


def make_stockmarket_table_white_borders():

    # Table-level style
    table_style_tiny = {
        "borderCollapse": "collapse",
        "borderSpacing": "0",
        "border": "1px solid #fff",  # White borders
        "margin": "0px",
        "padding": "0px",
        "fontSize": "10px",
        #"width": "80px",
    }

    # Row1
    row1_th_style = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#D9D9D9",  # grey #D9D9D9
        "color": "black",
        "width": "80px",
    }

    row1_th_style_1st = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "white",  # white
        "color": "black",
        "minWidth": "120px",
    }

    # change color of selected headers
    row1_th_style_lag = row1_th_style.copy()
    row1_th_style_sem = row1_th_style.copy()
    row1_th_style_amag = row1_th_style.copy()

    row1_th_style_lag['backgroundColor'] = '#82D535' # #82D535
    row1_th_style_sem['backgroundColor'] = '#203F65' # #203F65
    row1_th_style_sem['color'] = 'white' # white
    row1_th_style_amag['backgroundColor'] = '#8DB4E2' # #8DB4E2

    #row1_th_style['backgroundColor'] = 'white'

    #row1_th_style_sem = row1_th_style({'backgroundColor': '#203F65','color': 'white'}) # #203F65
    #row1_th_style_amag = row1_th_style({'backgroundColor': '#D9D9D9', 'color': 'black'}) # #8DB4E2


    row1 = html.Tr(
        [
            html.Th("", style=row1_th_style_1st),
            html.Th("ATX", colSpan=1, style=row1_th_style),
            html.Th("ATX prime", colSpan=1, style=row1_th_style),
            html.Th("DowJones", colSpan=1, style=row1_th_style),

            html.Th("EuroStocks50", colSpan=1, style=row1_th_style),
            html.Th("DAX", colSpan=1, style=row1_th_style),
            html.Th("SSE Comp.", colSpan=1, style=row1_th_style),

            html.Th("LAG", colSpan=1, style=row1_th_style_lag),
            html.Th("SEM", colSpan=1, style=row1_th_style_sem),
            html.Th("AMAG", colSpan=1, style=row1_th_style_amag),
        ],
        style={"margin": "0px", "padding": "0px", "width": "80px",},
    )


    # Data rows
    td_style_base2 = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "center",
        "backgroundColor": "#F2F4F1",  # white
        "color": "black",
        "width": "80px",
    }
    td_style_row_header2 = {
        "border": "1px solid #fff",
        "padding": "0px",
        "margin": "0px",
        "textAlign": "left",
        "backgroundColor": "white", # grey #F2F4F1
        "color": "black",
        "width": "80px",
    }

    data_trs2 = []
    for i, label in enumerate(stockmarket_row_labels):
        row_cells2 = []
        # Leftmost cell (row label):
        row_cells2.append(html.Td(label, style=td_style_row_header2))
        # Subsequent cells
        for val in stockmarket_data[i]:
            cell_style2 = td_style_base2.copy()
            row_cells2.append(html.Td(val, style=cell_style2))

        data_trs2.append(html.Tr(row_cells2, style={"margin": "0px", "padding": "0px"}))

    # Assemble the table
    return html.Table(
        [row1] + data_trs2,
        style=table_style_tiny,
    )





################################################################################
# DASH APP
################################################################################

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#app.layout = html.Div(
page2_table = html.Div(
    [
        html.H1(
            "Market Overview: LEN & SEM",
            style={
                "textAlign": "center",
                "margin": "0px",
                "padding": "0px",
                "fontSize": "16px",
            },
        ),

        # lenzing Table
        html.Div(
            [
                html.H3(
                    #"LEN",
                    style={
                        "backgroundColor": "white",
                        "color": "black",
                        "margin": "0px",
                        "padding": "4px",
                        "fontSize": "12px",
                    },
                ),
                make_lenzing_table_white_borders(),
            ],
            style={"margin": "10px", "padding": "0px"},
        ),

        #html.Br(),


        # SEM Table
        html.Div(
            [
                html.H3(
                    #"SEM",
                    style={
                        "backgroundColor": "#fff",
                        "color": "black",
                        "margin": "0px",
                        "padding": "4px",
                        "fontSize": "12px",
                    },
                ),
                make_semperit_table_white_borders(),
            ],
            style={"margin": "10px", "padding": "0px"},
        ),

        #html.Br(),


        # AMAG Table
        html.Div(
            [
                html.H3(
                    #"AMAG",
                    style={
                        "backgroundColor": "#fff",
                        "color": "black",
                        "margin": "0px",
                        "padding": "4px",
                        "fontSize": "12px",
                    },
                ),
                make_amag_table_white_borders(),
            ],
            style={"margin": "10px", "padding": "0px"},
        ),

        # Energy Table
        html.Div(
            [
                html.H3(
                    #"Energy",
                    style={
                        "backgroundColor": "#fff",
                        "color": "black",
                        "margin": "0px",
                        "padding": "4px",
                        "fontSize": "12px",
                    },
                ),
                make_energy_table_white_borders(),
            ],
            style={"margin": "10px", "padding": "0px"},
        ),


        # Stockmarket Table
        html.Div(
            [
                html.H3(
                    "Stock markets 1)",
                    style={
                        "backgroundColor": "white",
                        "font-weight": "bold",
                        "color": "#203F65",
                        "margin": "0px",
                        "padding": "1px",
                        "fontSize": "10px",
                    },
                ),
                make_stockmarket_table_white_borders(),
            ],
            style={"margin": "10px", "padding": "0px"},
        ),


    ],
    style={"margin": "0px", "padding": "0px"},
)

if __name__ == "__main__":
    app.run_server(debug=True)


#server = app.server







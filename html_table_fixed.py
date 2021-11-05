def html_fixed():
    import pandas as pd
    import webbrowser
    from exchange_rates_fixed import cur, exc_rat

    df = pd.DataFrame(exc_rat, cur)


    html = df.to_html(header=False)

    text_file = open("exchange_rates_for_2010-01-15.html", "w")
    text_file.write(html)
    text_file.close()

    webbrowser.open_new_tab('exchange_rates_for_2010-01-15.html')
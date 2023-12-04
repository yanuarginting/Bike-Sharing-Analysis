# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Setting Layout
st.set_page_config(layout="wide")

# Add Title and Tabs
st.title("Proyek Analisis Data: Bike Sharing Dataset")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["Pertanyaan 1", 
                                                                              "Pertanyaan 2", 
                                                                              "Pertanyaan 3", 
                                                                              "Pertanyaan 4", 
                                                                              "Pertanyaan 5", 
                                                                              "Pertanyaan 6", 
                                                                              "Pertanyaan 7", 
                                                                              "Pertanyaan 8", 
                                                                              "Pertanyaan 9", 
                                                                              "Pertanyaan 10", 
                                                                              "Pertanyaan 11"])

# Import Dataframe
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Change the Data Type of the "dteday" Column 
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Add Content to Tab
with tab1:
    st.header("Bagaimana tren penyewaan sepeda berdasarkan tahun?")

    yearly_df = day_df.resample("Y", on="dteday").sum()
    yearly_df = yearly_df.reset_index()
    
    yearly_df["dteday"] = ["2011", "2012"]

    plt.figure(figsize=(16, 8))
    plt.bar(yearly_df["dteday"], yearly_df["cnt"])

    for i in range(len(yearly_df["dteday"])):
        plt.text(i, yearly_df["cnt"][i], 
                 str(yearly_df["cnt"][i]), 
                 ha="center", va="bottom")

    plt.title("Bike Rental Trends by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Bike Rentals")

    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Terjadi kenaikan yang sangat masif, hal ini menandakan permintaan penyewaan sepeda mengalami peningkatan dari tahun ke tahun.")

# Add Content to Tab
with tab2:
    st.header("Bagaimana tren penyewaan sepeda berdasarkan kuartal?")

    quarterly_df = day_df.resample("Q", on="dteday").sum()
    quarterly_df = quarterly_df.reset_index()

    quarterly_df["dteday"] = ["1st Quarter (2011)", "2nd Quarter (2011)",
                              "3rd Quarter (2011)", "4th Quarter (2011)",
                              "1st Quarter (2012)", "2nd Quarter (2012)",
                              "3rd Quarter (2012)", "4th Quarter (2012)"]

    plt.figure(figsize=(16, 8))
    plt.plot(quarterly_df["dteday"], quarterly_df["cnt"])

    plt.title("Bike Rental Trends by Quarter")
    plt.xlabel("Quarter")
    plt.ylabel("Number of Bike Rentals")

    plt.grid(True)
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Ternyata terjadi kenaikan dan penurunan jika dilihat berdasarkan kuartal.")

# Add Content to Tab
with tab3:
    st.header("Bagaimana tren penyewaan sepeda berdasarkan bulan?")

    monthly_df = day_df.resample("M", on="dteday").sum()
    monthly_df = monthly_df.reset_index()

    monthly_df["dteday"] = ["Jan 2011", "Feb 2011", "Mar 2011",
                            "Apr 2011", "May 2011", "Jun 2011",
                            "Jul 2011", "Aug 2011", "Sep 2011",
                            "Oct 2011", "Nov 2011", "Dec 2011",
                            "Jan 2012", "Feb 2012", "Mar 2012",
                            "Apr 2012", "May 2012", "Jun 2012",
                            "Jul 2012", "Aug 2012", "Sep 2012",
                            "Oct 2012", "Nov 2012", "Dec 2012"]

    plt.figure(figsize=(16, 8))
    plt.plot(monthly_df["dteday"], monthly_df["cnt"])

    plt.title("Bike Rental Trends by Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Bike Rentals")

    plt.xticks(rotation=15)
    plt.grid(True)
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Terjadi kenaikan dan penurunan yang sangat signifikan dan hal tersebut terlihat lebih jelas jika dilihat berdasarkan bulan.")

# Add Content to Tab
with tab4:
    st.header("Pada musim apa penyewaan sepeda mengalami permintaan paling banyak dan paling sedikit?")

    seasonally_agg = day_df.groupby("season").agg({
        "instant": "nunique",
        "cnt": ["max", "min"]
    })
    seasonally_agg = seasonally_agg.reset_index()

    seasonally_agg["season"] = ["Spring", "Summer", "Fall", "Winter"]

    plt.figure(figsize=(16, 8))
    plt.bar(seasonally_agg["season"],
            seasonally_agg[("cnt", "max")],
            label="Max Rentals")
    plt.bar(seasonally_agg["season"],
            seasonally_agg[("cnt", "min")],
            label="Min Rentals")

    for i in range(len(seasonally_agg["season"])):
        plt.text(i, seasonally_agg[("cnt", "max")][i],
                 str(seasonally_agg[("cnt", "max")][i]),
                 ha="center", va="bottom")
        plt.text(i, seasonally_agg[("cnt", "min")][i],
                 str(seasonally_agg[("cnt", "min")][i]),
                 ha="center", va="bottom")

    plt.title("Max and Min Bike Rentals by Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Bike Rentals")

    plt.legend(loc="upper left")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Permintaan paling banyak ada pada **musim gugur** yaitu sebesar **8714**, sedangkan permintaan paling sedikit ada pada **musim dingin** yaitu sebesar **22**.")

# Add Content to Tab
with tab5:
    st.header("Pada bulan apa penyewaan sepeda mengalami permintaan paling banyak dan paling sedikit?")

    monthly_agg = day_df.groupby("mnth").agg({
        "instant": "nunique",
        "cnt": ["max", "min"]
    })
    monthly_agg = monthly_agg.reset_index()

    monthly_agg["mnth"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.figure(figsize=(16, 8))
    plt.bar(monthly_agg["mnth"],
            monthly_agg[("cnt", "max")],
            label="Max Rentals")
    plt.bar(monthly_agg["mnth"],
            monthly_agg[("cnt", "min")],
            label="Min Rentals")

    for i in range(len(monthly_agg["mnth"])):
        plt.text(i, monthly_agg[("cnt", "max")][i],
                 str(monthly_agg[("cnt", "max")][i]),
                 ha="center", va="bottom")
        plt.text(i, monthly_agg[("cnt", "min")][i],
                 str(monthly_agg[("cnt", "min")][i]),
                 ha="center", va="bottom")

    plt.title("Max and Min Bike Rentals by Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Bike Rentals")

    plt.legend(loc="upper left")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Permintaan paling banyak ada pada **bulan september** yaitu sebesar **8714**, sedangkan permintaan paling sedikit ada pada **bulan oktober** yaitu sebesar **22**.")

# Add Content to Tab
with tab6:
    st.header("Pada hari kerja atau akhir pekan penyewaan sepeda mengalami permintaan paling banyak dan paling sedikit?")

    weekdays_or_weekends_agg = day_df.groupby("workingday").agg({
        "instant": "nunique",
        "cnt": ["max", "min"]
    })
    weekdays_or_weekends_agg = weekdays_or_weekends_agg.reset_index()

    weekdays_or_weekends_agg["workingday"] = ["Weekends", "Weekdays"]

    plt.figure(figsize=(16, 8))
    plt.bar(weekdays_or_weekends_agg["workingday"],
            weekdays_or_weekends_agg[("cnt", "max")],
            label="Max Rentals")
    plt.bar(weekdays_or_weekends_agg["workingday"],
            weekdays_or_weekends_agg[("cnt", "min")],
            label="Min Rentals")

    for i in range(len(weekdays_or_weekends_agg["workingday"])):
        plt.text(i, weekdays_or_weekends_agg[("cnt", "max")][i],
                 str(weekdays_or_weekends_agg[("cnt", "max")][i]),
                 ha="center", va="bottom")
        plt.text(i, weekdays_or_weekends_agg[("cnt", "min")][i],
                 str(weekdays_or_weekends_agg[("cnt", "min")][i]),
                 ha="center", va="bottom")

    plt.title("Max and Min Bike Rentals by Weekdays and Weekends")
    plt.ylabel("Number of Bike Rentals")

    plt.legend(loc="upper left")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Permintaan paling banyak ada pada **akhir pekan** yaitu sebesar **8714**, sedangkan permintaan paling sedikit ada pada **hari kerja** yaitu sebesar **22**.")

# Add Content to Tab
with tab7:
    st.header("Pada hari libur atau bukan penyewaan sepeda mengalami permintaan paling banyak dan paling sedikit?")

    holiday_agg = day_df.groupby("holiday").agg({
        "instant": "nunique",
        "cnt": ["max", "min"]
    })
    holiday_agg = holiday_agg.reset_index()

    holiday_agg["holiday"] = ["Not Holiday", "Holiday"]

    plt.figure(figsize=(16, 8))
    plt.bar(holiday_agg["holiday"],
            holiday_agg[("cnt", "max")],
            label="Max Rentals")
    plt.bar(holiday_agg["holiday"],
            holiday_agg[("cnt", "min")],
            label="Min Rentals")

    for i in range(len(holiday_agg["holiday"])):
        plt.text(i, holiday_agg[("cnt", "max")][i],
                 str(holiday_agg[("cnt", "max")][i]),
                 ha="center", va="bottom")
        plt.text(i, holiday_agg[("cnt", "min")][i],
                 str(holiday_agg[("cnt", "min")][i]),
                 ha="center", va="bottom")

    plt.title("Max and Min Bike Rentals by Holidays and Not Holiday")
    plt.ylabel("Number of Bike Rentals")

    plt.legend(loc="upper left")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Permintaan paling banyak ada pada **bukan hari libur** yaitu sebesar **8714**, sedangkan permintaan paling sedikit ada pada **bukan hari libur** juga yaitu sebesar **22**.")

# Add Content to Tab
with tab8:
    st.header("Pada hari apa penyewaan sepeda mengalami permintaan paling banyak dan paling sedikit?")

    daily_agg = day_df.groupby("weekday").agg({
        "instant": "nunique",
        "cnt": ["max", "min"]
    })
    daily_agg = daily_agg.reset_index()

    daily_agg["weekday"] = ["Sunday", "Monday", "Tuesday", "Wednesday",
                            "Thursday", "Friday", "Saturday"]

    plt.figure(figsize=(16, 8))
    plt.bar(daily_agg["weekday"],
            daily_agg[("cnt", "max")],
            label="Max Rentals")
    plt.bar(daily_agg["weekday"],
            daily_agg[("cnt", "min")],
            label="Min Rentals")

    for i in range(len(daily_agg["weekday"])):
        plt.text(i, daily_agg[("cnt", "max")][i],
                 str(daily_agg[("cnt", "max")][i]),
                 ha="center", va="bottom")
        plt.text(i, daily_agg[("cnt", "min")][i],
                 str(daily_agg[("cnt", "min")][i]),
                 ha="center", va="bottom")

    plt.title("Max and Min Bike Rentals by Day")
    plt.xlabel("Day")
    plt.ylabel("Number of Bike Rentals")

    plt.legend(loc="upper left")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Permintaan paling banyak ada pada **hari sabtu** yaitu sebesar **8714**, sedangkan permintaan paling sedikit ada pada **hari senin** juga yaitu sebesar **22**.")

# Add Content to Tab
with tab9:
    st.header("Pada cuaca apa penyewaan sepeda mengalami permintaan paling banyak dan paling sedikit?")

    weather_agg = day_df.groupby("weathersit").agg({
        "instant": "nunique",
        "cnt": ["max", "min"]
    })
    weather_agg = weather_agg.reset_index()

    weather_agg["weathersit"] = ["Sunny", "Cloudy", "Light Rain"]

    plt.figure(figsize=(16, 8))
    plt.bar(weather_agg["weathersit"],
            weather_agg[("cnt", "max")],
            label="Max Rentals")
    plt.bar(weather_agg["weathersit"],
            weather_agg[("cnt", "min")],
            label="Min Rentals")

    for i in range(len(weather_agg["weathersit"])):
        plt.text(i, weather_agg[("cnt", "max")][i],
                 str(weather_agg[("cnt", "max")][i]),
                 ha="center", va="bottom")
        plt.text(i, weather_agg[("cnt", "min")][i],
                 str(weather_agg[("cnt", "min")][i]),
                 ha="center", va="bottom")

    plt.title("Max and Min Bike Rentals by Weather")
    plt.xlabel('Weather')
    plt.ylabel("Number of Bike Rentals")

    plt.legend(loc="upper left")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Permintaan paling banyak ada pada **cuaca cerah** yaitu sebesar **8714**, sedangkan permintaan paling sedikit ada pada **cuaca hujan ringan** juga yaitu sebesar **22**.")

# Add Content to Tab
with tab10:
    st.header("Pada jam berapa penyewaan sepeda mengalami permintaan paling banyak dan paling sedikit?")

    hourly_agg = hour_df.groupby("hr").agg({
        "instant": "nunique",
        "cnt": ["max", "min"]
    })
    hourly_agg = hourly_agg.reset_index()

    hourly_agg["hr"] = ["12 PM", "01 AM", "02 AM", "03 AM", "04 AM", "05 AM",
                        "06 AM", "07 AM", "08 AM", "09 AM", "10 AM", "11 AM",
                        "12 AM", "01 PM", "02 PM", "03 PM", "04 PM", "05 PM",
                        "06 PM", "07 PM", "08 PM", "09 PM", "10 PM", "11 PM"]

    plt.figure(figsize=(16, 8))
    plt.bar(hourly_agg["hr"],
            hourly_agg[("cnt", "max")],
            label="Max Rentals")
    plt.bar(hourly_agg["hr"],
            hourly_agg[("cnt", "min")],
            label="Min Rentals")

    for i in range(len(hourly_agg["hr"])):
        plt.text(i, hourly_agg[("cnt", "max")][i],
                 str(hourly_agg[("cnt", "max")][i]),
                 ha="center", va="bottom")
        plt.text(i, hourly_agg[("cnt", "min")][i],
                 str(hourly_agg[("cnt", "min")][i]),
                 ha="center", va="bottom")

    plt.title("Max and Min Bike Rentals by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Number of Bike Rentals")

    plt.legend(loc="upper left")
    plt.xticks(rotation=25)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Permintaan paling banyak ada pada **jam 6 sore** yaitu sebesar **977**, sedangkan permintaan paling sedikit ada pada **jam 1 sampai jam 7 pagi** juga yaitu sebesar **1**.")

# Add Content to Tab
with tab11:
    st.header("Apa tipe pengguna paling banyak dalam penyewaan sepeda?")

    users = ["Casual", "Registered"]

    plt.figure(figsize=(16, 8))
    plt.bar(users, day_df[["casual", "registered"]].sum())

    for i in range(len(users)):
        plt.text(i, day_df[["casual", "registered"]].sum()[i],
                 str(day_df[["casual", "registered"]].sum()[i]),
                 ha="center", va="bottom")

    plt.title("Bike Rentals by User Type")
    plt.xlabel("User")
    plt.ylabel("Number of Bike Rentals")

    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    st.pyplot(plt)

    st.caption("Kesimpulan: Tipe pengguna paling banyak ada pada pengguna yang terdaftar.")
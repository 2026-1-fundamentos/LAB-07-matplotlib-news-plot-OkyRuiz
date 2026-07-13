"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    df = pd.read_csv("files/input/news.csv", index_col=0)

    colors = {
        "Television": "dimgrey",
        "Newspaper": "grey",
        "Radio": "lightgrey",
        "Internet": "tab:blue",
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Radio": 1,
        "Internet": 2,
    }

    linewidth = {
        "Television": 1,
        "Newspaper": 1,
        "Radio": 1,
        "Internet": 4,
    }

    plt.figure(figsize=(6, 4))

    for col in df.columns:
        plt.plot(
            df[col],
            label=col,
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidth[col],
        )

    plt.title("People get news from", fontsize=16)

    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.yaxis.set_visible(False)

    first_year = df.index[0]
    last_year = df.index[-1]

    for col in df.columns:
        first_value = df[col].iloc[0]
        last_value = df[col].iloc[-1]

        plt.scatter(first_year, first_value, color=colors[col])
        plt.text(
            first_year - 0.2,
            first_value,
            f"{col}  {first_value}%",
            color=colors[col],
            ha="right",
            va="center",
        )

        plt.scatter(last_year, last_value, color=colors[col])
        plt.text(
            last_year + 0.2,
            last_value,
            f"{last_value}%",
            color=colors[col],
            ha="left",
            va="center",
        )

    plt.xticks(df.index, [str(y) for y in df.index], ha="center")
    plt.tight_layout()

    os.makedirs("files/plots", exist_ok=True)
    plt.savefig("files/plots/news.png")
    plt.close()

if __name__ == "__main__":
    pregunta_01()

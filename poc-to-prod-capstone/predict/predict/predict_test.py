from predict.predict.run import TextPredictionModel  # Update the import path if necessary

def main():
    artefacts_path = 'C:\\Data engineering 4th year\\Poc to prod\\poc-to-prod-capstone\\train\\data\\artefacts'
    text_to_predict = "Type your title here..."

    model = TextPredictionModel.from_artefacts(artefacts_path)
    predictions = model.predict([text_to_predict])

    print(f'Predictions for `{text_to_predict}`:')
    print(predictions)

if __name__ == "__main__":
    main()

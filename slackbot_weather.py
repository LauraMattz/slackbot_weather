import time

# Run the loop for five minutes
end_time = time.time() + 60 * 5
while time.time() < end_time:
    # Load the page with weather information
    html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content

    # Parse the HTML of the page
    soup = BeautifulSoup(html, 'html.parser')

    # Capture data by navigating the HTML elements
    resume = soup.find(class_='-gray -line-height-24 _center')
    temp_min = soup.find(id='min-temp-1')
    temp_max = soup.find(id='max-temp-1')

    # Print the results
    print('\n Resumo: ' + resume.text)
    print(' Temp. Mínima: ' + temp_min.string)
    print(' Temp. Máxima: ' + temp_max.string)

    # Build the message to send to Slack
    message = {
        "text": f"Sobre a temperatura de São Paulo hoje: {resume.text}\nTemp. Mínima: {temp_min.string}\nTemp. Máxima: {temp_max.string}"
    }

    # Send the message to Slack
    webhook_url = " "
    requests.post(webhook_url, json=message)

    # Wait one minute before running the loop again
    time.sleep(60)

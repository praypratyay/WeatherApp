const DJANGO_API_URL = 'http://localhost:8000/api'; 

export async function fetchWeatherData(cityName) {
  try {
    let [weatherPromise] = await Promise.all([
      fetch(
        `${DJANGO_API_URL}/${cityName}`
      ),
    ]);
    
    const weatherResponse = await weatherPromise.json();
    return [weatherResponse];
  } catch (error) {
    console.log(error);
  }
}


import React from 'react';
import ErrorBox from '../../Reusable/ErrorBox';
import AirConditionsItem from './AirConditionsItem';
import Layout from '../../Reusable/Layout';

const TodayWeatherAirConditions = ({ data }) => {
  const noDataProvided =
    !data || Object.keys(data).length === 0 || data.cod === '404';

  let content = <ErrorBox flex="1" type="error" />;

  if (!noDataProvided)
    content = (
      <>
        <AirConditionsItem
          title="Feels Like"
          value={`${Math.round(data.weather.main.feels_like)} °C`}
        />
        <AirConditionsItem
          title="Wind"
          value={`${data.weather.wind.speed} m/s`}
        />
        <AirConditionsItem
          title="Clouds"
          value={`${Math.round(data.weather.clouds.all)} %`}
        />
        <AirConditionsItem
          title="Humidity"
          value={`${Math.round(data.weather.main.humidity)} %`}
        />
      </>
    );
  return (
    <Layout
      title="CONDITIONS"
      content={content}
      mb="1rem"
      sx={{ marginTop: '2.9rem' }}
    />
  );
};

export default TodayWeatherAirConditions;

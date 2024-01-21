import React from 'react';
import ErrorBox from '../../Reusable/ErrorBox';
import AirConditionsItem from '../AirConditions/AirConditionsItem';
import Layout from '../../Reusable/Layout';

const AirQuailty = ({ data }) => {
  const noDataProvided =
    !data || Object.keys(data).length === 0 || data.cod === '404';

  let content = <ErrorBox flex="1" type="error" />;

  if (!noDataProvided)
    content = (
 
        <AirConditionsItem
          title="AQI"
          value={`${data.air_quality.main.aqi}`}
        />
  
    );
  return (
    <Layout
      title="AIR QUALITY INDEX"
      content={content}
      mb="1rem"
      sx={{ marginTop: '3rem' }}
    />
  );
};

export default AirQuailty;

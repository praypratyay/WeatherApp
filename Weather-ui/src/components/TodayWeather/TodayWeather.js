import { Grid } from '@mui/material';
import React from 'react';
import AirConditions from './AirConditions/AirConditions';
import Details from './Details/Details';
import AirQuality from './AirQuality/AirQuailty';

const TodayWeather = ({ data }) => {
  return (
    <Grid container sx={{ padding: '3rem 0rem 0rem' }}>
      <Details data={data} />
      <AirConditions data={data} />
      <AirQuality data={data} />
    </Grid>
  );
};

export default TodayWeather;

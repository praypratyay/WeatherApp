import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import { Bar} from 'react-chartjs-2';
import SectionHeader from '../Reusable/SectionHeader';

import Chart from 'chart.js/auto';

const PollutantConcentration = ({ data }) => {
  const chartData = {
    labels: ['SO2', 'NO2', 'PM10', 'PM2_5', 'O3', 'CO'],
    datasets: [
      {
        label: 'Levels',
        data: [
          data?.air_quality?.components?.so2,
          data?.air_quality?.components?.no2,
          data?.air_quality?.components?.pm10,
          data?.air_quality?.components?.pm2_5,
          data?.air_quality?.components?.o3,
          data?.air_quality?.components?.co,
        ],
        backgroundColor: 'white',
        borderColor: 'black',
        borderWidth: 1,
        
      },
    ],
  };

  const chartOptions = {
    indexAxis: 'y',
    scales: {
      x: {
        ticks : {
          color: "black",
        },
        beginAtZero: true,

      },
      y: {
        labels: ['SO2', 'NO2', 'PM10', 'PM2_5', 'O3', 'CO'],
        type: 'category',
        ticks : {
          color: "black",
        },
      },
    },
    plugins: {
      tooltip: {
        callbacks: {
          label: (context) => {
            const value = context.parsed.x || 0;
            const pollutant = String(context.label).toLowerCase()
            const qualitativeName = data?.air_quality?.QualitativeNames?.[pollutant];
            return `${value} μg/m³ - ${qualitativeName}`;
          },
        },
      },
    },
  };

  return (
    <Container>
      <Row className="mt-5">
        <Col md={7}>
        <SectionHeader title="Pollutant Concentration Levels"mb={"1rem" || '0'} />
          <Bar data={chartData} options={chartOptions} />
        </Col>
      </Row>
    </Container>
  );



};

export default PollutantConcentration;

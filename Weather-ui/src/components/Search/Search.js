import React, { useState } from 'react';

const Search = ({ onSearchChange }) => {
  const [searchValue, setSearchValue] = useState('');

  const handleChange = (event) => {
    const value = event.target.value;
    setSearchValue(value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onSearchChange(searchValue);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter city name ..."
        value={searchValue}
        onChange={handleChange}
      />
      <button  type="submit">GO</button>
    </form>
  );
};

export default Search;

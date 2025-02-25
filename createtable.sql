-- create a table to store data from GRIB files. This example for N location or North.

CREATE TABLE IF NOT EXISTS `meteorological_data_N` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `temp` FLOAT NULL,
  `dewtemp` FLOAT NULL,
  `precip` FLOAT NULL,
  `humid` FLOAT NULL,
  `location` VARCHAR(45) NULL,
  `date_time` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB

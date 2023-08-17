# Custom Web Scraper README

## Overview

This custom web scraper was designed to meet the specific needs of a small business, allowing them to save certifications acquired by their clients from an e-learning platform before access was lost.

## Approach

The web scraper was developed within a tight timeframe of 6 hours, resulting in a relatively simple and straightforward design. Although optimization was limited due to time constraints, some modifications were introduced to address common bugs.

## Functionality

The scraper uses the Edge WebDriver to mimic user actions such as logging in, clicking, and downloading. Given the large volume of data – approximately 6500 users with multiple certifications spread across 150 pages – the session could occasionally timeout, necessitating a restart of the script from the last processed page. To avoid duplication, entries from the current page were deleted.

## Considerations

It's important to understand that this application prioritized rapid response over optimization. As a result, aspects like web scraping efficiency, delays, and other code segments were not extensively refined. The primary objective was to create a solution that functioned as swiftly as possible and maintained partial consistency to fulfill the immediate requirements.

## Usage Caution

Users intending to employ this script should do so with full awareness of its nature. It was developed under time pressure and may not conform to best practices or the highest coding standards. Deploy this script at your own discretion and risk.
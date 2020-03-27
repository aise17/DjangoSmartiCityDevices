import { Component, OnInit } from '@angular/core';


import { NgZone } from "@angular/core";
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import * as am4maps from "@amcharts/amcharts4/maps";

import am4geodata_worldLow from "@amcharts/amcharts4-geodata/worldLow";

am4core.useTheme(am4themes_animated);



@Component({
  selector: 'app-dashboard-devices',
  templateUrl: './dashboard-devices.page.html',
  styleUrls: ['./dashboard-devices.page.scss'],
})
export class DashboardDevicesPage implements OnInit {

 

  private topChartdevice: am4charts.XYChart;
  private firstlinedevice: am4charts.XYChart;
  private secondlinedevice: am4charts.XYChart;
  private thirdlinedevice: am4charts.XYChart;

  private colors = new am4core.ColorSet();


  constructor(
    private zone: NgZone
  ) { }

  ngOnInit() {
  }


  ngAfterViewInit() {
    console.log('holav------------------------------------------')

    this.createTopChart();
    console.log('holav***********************')

    this.createLine("cardlinefirstdevice" ,[
      { "date": new Date(2018, 0, 1, 8, 0, 0), "value": 57 },
      { "date": new Date(2018, 0, 1, 9, 0, 0), "value": 27 },
      { "date": new Date(2018, 0, 1, 10, 0, 0), "value": 24 },
      { "date": new Date(2018, 0, 1, 11, 0, 0), "value": 59 },
      { "date": new Date(2018, 0, 1, 12, 0, 0), "value": 33 },
      { "date": new Date(2018, 0, 1, 13, 0, 0), "value": 46 },
      { "date": new Date(2018, 0, 1, 14, 0, 0), "value": 20 },
      { "date": new Date(2018, 0, 1, 15, 0, 0), "value": 42 },
      { "date": new Date(2018, 0, 1, 16, 0, 0), "value": 59, "opacity": 1}
     ], this.colors.getIndex(0));


     this.createLine("cardlineseconddevice" ,[
      { "date": new Date(2018, 0, 1, 8, 0, 0), "value": 57 },
      { "date": new Date(2018, 0, 1, 9, 0, 0), "value": 27 },
      { "date": new Date(2018, 0, 1, 10, 0, 0), "value": 24 },
      { "date": new Date(2018, 0, 1, 11, 0, 0), "value": 59 },
      { "date": new Date(2018, 0, 1, 12, 0, 0), "value": 33 },
      { "date": new Date(2018, 0, 1, 13, 0, 0), "value": 46 },
      { "date": new Date(2018, 0, 1, 14, 0, 0), "value": 20 },
      { "date": new Date(2018, 0, 1, 15, 0, 0), "value": 42 },
      { "date": new Date(2018, 0, 1, 16, 0, 0), "value": 59, "opacity": 1}
     ], this.colors.getIndex(1));

     this.createLine("cardlinethirddevice" ,[
      { "date": new Date(2018, 0, 1, 8, 0, 0), "value": 57 },
      { "date": new Date(2018, 0, 1, 9, 0, 0), "value": 27 },
      { "date": new Date(2018, 0, 1, 10, 0, 0), "value": 24 },
      { "date": new Date(2018, 0, 1, 11, 0, 0), "value": 59 },
      { "date": new Date(2018, 0, 1, 12, 0, 0), "value": 33 },
      { "date": new Date(2018, 0, 1, 13, 0, 0), "value": 46 },
      { "date": new Date(2018, 0, 1, 14, 0, 0), "value": 20 },
      { "date": new Date(2018, 0, 1, 15, 0, 0), "value": 42 },
      { "date": new Date(2018, 0, 1, 16, 0, 0), "value": 59, "opacity": 1}
     ], this.colors.getIndex(20));
     


  }

  ngOnDestroy() {
    this.zone.runOutsideAngular(() => {
      if (this.topChartdevice) {
        this.topChartdevice.dispose();
      }
      if (this.firstlinedevice) {
        this.firstlinedevice.dispose();
      }

    });
  }


  createTopChart(){
  

    this.zone.runOutsideAngular(() => {

      let targetSVG = "M9,0C4.029,0,0,4.029,0,9s4.029,9,9,9s9-4.029,9-9S13.971,0,9,0z M9,15.93 c-3.83,0-6.93-3.1-6.93-6.93S5.17,2.07,9,2.07s6.93,3.1,6.93,6.93S12.83,15.93,9,15.93 M12.5,9c0,1.933-1.567,3.5-3.5,3.5S5.5,10.933,5.5,9S7.067,5.5,9,5.5 S12.5,7.067,12.5,9z";

// Create map instance
let chart = am4core.create("chartdivdevices", am4maps.MapChart);
let interfaceColors = new am4core.InterfaceColorSet();

// Set map definition
chart.geodata = am4geodata_worldLow;

// Set projection
chart.projection = new am4maps.projections.Mercator();

// Add zoom control
chart.zoomControl = new am4maps.ZoomControl();

// Set initial zoom
chart.homeZoomLevel = 2.5;
chart.homeGeoPoint = {
  latitude: 51,
  longitude: -23
};

// Create map polygon series
let polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
polygonSeries.exclude = ["AQ"];
polygonSeries.useGeodata = true;
polygonSeries.mapPolygons.template.nonScalingStroke = true;

// Add images
let imageSeries = chart.series.push(new am4maps.MapImageSeries());
let imageTemplate = imageSeries.mapImages.template;
imageTemplate.tooltipText = "{title}";
imageTemplate.nonScaling = true;

let marker = imageTemplate.createChild(am4core.Sprite);
marker.path = targetSVG;
marker.horizontalCenter = "middle";
marker.verticalCenter = "middle";
marker.scale = 0.7;
marker.fill = interfaceColors.getFor("alternativeBackground");

imageTemplate.propertyFields.latitude = "latitude";
imageTemplate.propertyFields.longitude = "longitude";
imageSeries.data = [ {
  "id": "london",
  "svgPath": targetSVG,
  "title": "London",
  "latitude": 51.5002,
  "longitude": -0.1262,
  "scale": 1
}, {
  "svgPath": targetSVG,
  "title": "Brussels",
  "latitude": 50.8371,
  "longitude": 4.3676,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Prague",
  "latitude": 50.0878,
  "longitude": 14.4205,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Athens",
  "latitude": 37.9792,
  "longitude": 23.7166,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Reykjavik",
  "latitude": 64.1353,
  "longitude": -21.8952,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Dublin",
  "latitude": 53.3441,
  "longitude": -6.2675,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Oslo",
  "latitude": 59.9138,
  "longitude": 10.7387,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Lisbon",
  "latitude": 38.7072,
  "longitude": -9.1355,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Moscow",
  "latitude": 55.7558,
  "longitude": 37.6176,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Belgrade",
  "latitude": 44.8048,
  "longitude": 20.4781,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Bratislava",
  "latitude": 48.2116,
  "longitude": 17.1547,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Ljubljana",
  "latitude": 46.0514,
  "longitude": 14.5060,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Madrid",
  "latitude": 40.4167,
  "longitude": -3.7033,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Stockholm",
  "latitude": 59.3328,
  "longitude": 18.0645,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Bern",
  "latitude": 46.9480,
  "longitude": 7.4481,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Kiev",
  "latitude": 50.4422,
  "longitude": 30.5367,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "Paris",
  "latitude": 48.8567,
  "longitude": 2.3510,
  "scale": 0.5
}, {
  "svgPath": targetSVG,
  "title": "New York",
  "latitude": 40.43,
  "longitude": -74,
  "scale": 0.5
} ];

// Add lines
let lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.dataFields.multiGeoLine = "multiGeoLine";

let lineTemplate = lineSeries.mapLines.template;
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 4;
lineTemplate.arrow.height = 6;
lineTemplate.stroke = interfaceColors.getFor("alternativeBackground");
lineTemplate.fill = interfaceColors.getFor("alternativeBackground");
lineTemplate.line.strokeOpacity = 0.4;

lineSeries.data = [{
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 50.4422, "longitude": 30.5367 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 40.4300, "longitude": -74.0000 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 64.1353, "longitude": -21.8952 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 37.9792, "longitude": 23.7166 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 38.7072, "longitude": -9.1355 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 55.7558, "longitude": 37.6176 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 44.8048, "longitude": 20.4781 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 48.2116, "longitude": 17.1547 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 46.0514, "longitude": 14.5060 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 40.4167, "longitude": -3.7033 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 59.3328, "longitude": 18.0645 }
    ]
  ]
}, {
  "multiGeoLine": [
    [
      { "latitude": 51.5002, "longitude": -0.1262 },
      { "latitude": 46.9480, "longitude": 7.4481 }
    ]
  ]
}];

    });
  }


  createLine(divname, data, color) {

    let chart = am4core.create(divname, am4charts.XYChart);
    chart.width = am4core.percent(100);
    chart.height = 100;

    chart.data = data;

    

    let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.renderer.grid.template.disabled = true;
    dateAxis.renderer.labels.template.disabled = true;
    dateAxis.startLocation = 0.5;
    dateAxis.endLocation = 0.7;
    dateAxis.cursorTooltipEnabled = false;

    let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.min = 0;
    valueAxis.renderer.grid.template.disabled = true;
    valueAxis.renderer.baseGrid.disabled = true;
    valueAxis.renderer.labels.template.disabled = true;
    valueAxis.cursorTooltipEnabled = false;

    chart.cursor = new am4charts.XYCursor();
    chart.cursor.lineY.disabled = true;
    chart.cursor.behavior = "none";

    let series = chart.series.push(new am4charts.LineSeries());
    series.tooltipText = "{date}: [bold]{value}";
    series.dataFields.dateX = "date";
    series.dataFields.valueY = "value";
    series.tensionX = 0.8;
    series.strokeWidth = 5;
    series.stroke = color;

 

    return chart;
  }
}

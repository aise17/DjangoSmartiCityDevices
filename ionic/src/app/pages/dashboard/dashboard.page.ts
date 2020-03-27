import { Component, OnInit } from '@angular/core';
import { NgModule } from '@angular/core';

import { NgZone } from "@angular/core";
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";


am4core.useTheme(am4themes_animated);




@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.page.html',
  styleUrls: ['./dashboard.page.scss'],
})
export class DashboardPage implements OnInit {



  private topChart: am4charts.XYChart;
  private firstline: am4charts.XYChart;
  private secondline: am4charts.XYChart;
  private thirdline: am4charts.XYChart;

  private colors = new am4core.ColorSet();


  constructor(
    private zone: NgZone
  ) { }

  ngOnInit() {
  }


  ngAfterViewInit() {
    console.log('holav------------------------------------------')

    this.createTopChart();


    this.createLine("cardlinefirst" ,[
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


     this.createLine("cardlinesecond" ,[
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

     this.createLine("cardlinethird" ,[
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
      if (this.topChart) {
        this.topChart.dispose();
      }
      if (this.firstline) {
        this.firstline.dispose();
      }
    });
  }


  createTopChart(){
  

    this.zone.runOutsideAngular(() => {
      let chart = am4core.create("chartdiv", am4charts.XYChart);
  
      chart.paddingRight = 20;
  
      let data = [];
      let visits = 10;
      for (let i = 1; i < 366; i++) {
        visits += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 10);
        data.push({ date: new Date(2018, 0, i), name: "name" + i, value: visits });
      }
  
      chart.data = data;
  
      let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
      dateAxis.renderer.grid.template.location = 0;
  
      let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
      valueAxis.tooltip.disabled = true;
      valueAxis.renderer.minWidth = 35;
  
      let series = chart.series.push(new am4charts.LineSeries());
      series.dataFields.dateX = "date";
      series.dataFields.valueY = "value";
  
      series.tooltipText = "{valueY.value}";
      chart.cursor = new am4charts.XYCursor();
  
      let scrollbarX = new am4charts.XYChartScrollbar();
      scrollbarX.series.push(series);
      chart.scrollbarX = scrollbarX;
      chart.scrollbarX.parent = chart.bottomAxesContainer;

  
      this.topChart = chart;
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



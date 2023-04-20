# Databricks notebook source

dbutils.widgets.text('x', '1')
print(dbutils.widgets.get('x'))

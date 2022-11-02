---
title: Opensource
nav:
  order: 6
  tooltip: 开源项目与数据
---

# <i class="fas fa-tools"></i>Opensource 开源项目与数据

{%
  include link.html
  type="github"
  icon=""
  text="Follow us on GitHub"
  link="THUIR"
  style="button"
%}

{% include search-info.html %}

{% include section.html %}

## Toolkits

{% include list.html component="card" data="tools" filters="group: toolkit" %}

{% include section.html %}

## Datasets

{% include list.html component="projects" data="tools" filters="group: dataset" style="rich" %}

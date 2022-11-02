---
title: People
nav:
  order: 1
  tooltip: 团队成员
---

# <i class="fas fa-users"></i>Current 在校成员

## Faculty 教师

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pi"
%}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: engineer"
%}

{% include section.html %}

## Ph.D. Students 博士生

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}

{% include section.html %}

## Master Students 硕士生

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: master"
%}

{% include section.html %}

## PostDocs 博士后

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc"
%}

{% include section.html %}

## Staff and Project Managers 工作人员

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: staff"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pm"
%}
{:.center}

{% include section.html %}

# <i class="fas fa-users"></i>Alumni 毕业校友

{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: pi"
%}
{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: phd"
%}
{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: master"
%}
{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: postdoc"
%}
{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: staff"
%}
{:.center}

{% include section.html %}

Special thanks to [Jia Chen](https://xuanyuan14.github.io) and [Yan Fang](https://suffoquer-fang.github.io) for the initial construction of this page.

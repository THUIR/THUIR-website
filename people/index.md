---
title: People
nav:
  order: 1
  tooltip: 团队成员
---

# <i class="fas fa-users"></i>Current

{% include section.html %}

## Faculty

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

## Graduate Students

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: master"
%}

## PostDoc

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc"
%}

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: staff"
%}
{:.center}

{% include section.html %}

# <i class="fas fa-users"></i>Alumni

{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: pi"
%}

{% include section.html %}

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


{% include section.html background="images/banner.jpg" dark=true%}

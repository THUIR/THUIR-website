---
title: People
nav:
  order: 1
  tooltip: 团队成员
---

# <i class="fas fa-users"></i>Current

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

## Ph.D. Students

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}

{% include section.html %}

## Master Students

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: master"
%}

{% include section.html %}

## PostDocs

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc"
%}

{% include section.html %}

# <i class="fas fa-users"></i>Alumni

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


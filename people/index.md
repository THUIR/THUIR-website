---
title: People
nav:
  order: 1
  tooltip: 团队成员
---

# <i class="fas fa-users"></i>Current 在校成员

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

{% include section.html %}
## PostDoc

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc"
%}

{% include section.html %}

## Staff

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: staff"
%}
{:.center}

{% include section.html %}

# <i class="fas fa-users"></i>Alumni 实验室校友

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


/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* libmspub
 * Version: MPL 1.1 / GPLv2+ / LGPLv2+
 *
 * The contents of this file are subject to the Mozilla Public License Version
 * 1.1 (the "License"); you may not use this file except in compliance with
 * the License or as specified alternatively below. You may obtain a copy of
 * the License at http://www.mozilla.org/MPL/
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 * for the specific language governing rights and limitations under the
 * License.
 *
 * Major Contributor(s):
 * Copyright (C) 2012 Brennan Vincent <brennanv@email.arizona.edu>
 *
 * All Rights Reserved.
 *
 * For minor contributions see the git repository.
 *
 * Alternatively, the contents of this file may be used under the terms of
 * either the GNU General Public License Version 2 or later (the "GPLv2+"), or
 * the GNU Lesser General Public License Version 2 or later (the "LGPLv2+"),
 * in which case the provisions of the GPLv2+ or the LGPLv2+ are applicable
 * instead of those above.
 */

#ifndef __COORDINATE_H__
#define __COORDINATE_H__
#include "MSPUBConstants.h"
namespace libmspub
{
struct Coordinate
{
  Coordinate(int xs, int ys, int xe, int ye) : m_xs(xs), m_ys(ys), m_xe(xe), m_ye(ye) { }
  Coordinate() : m_xs(0), m_ys(0), m_xe(0), m_ye(0) { }
  int m_xs, m_ys, m_xe, m_ye;
  double getXIn(double pageWidth) const
  {
    return pageWidth / 2 + double(m_xs) / EMUS_IN_INCH;
  }
  double getYIn(double pageHeight) const
  {
    return pageHeight / 2 + double(m_ys) / EMUS_IN_INCH;
  }
  double getWidthIn() const
  {
    return double(m_xe - m_xs) / EMUS_IN_INCH;
  }
  double getHeightIn() const
  {
    return double(m_ye - m_ys) / EMUS_IN_INCH;
  }
};
}
#endif
/* vim:set shiftwidth=2 softtabstop=2 expandtab: */

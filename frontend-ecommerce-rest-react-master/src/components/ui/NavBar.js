import React from 'react';
import { Link } from "react-router-dom";

export const NavBar = () => {
    return (
        <>
            <div className="main-menu-area mg-tb-40">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <ul className="nav nav-tabs notika-menu-wrap menu-it-icon-pro">
                                <li className="active"><a data-toggle="tab" href="#Home"><i className="notika-icon notika-house"></i>
                                        Home</a>
                                </li>
                                <li><a data-toggle="tab" href="#profile"><i className="notika-icon notika-support"></i> User</a>
                                </li>
                                <li><a data-toggle="tab" href="#products"><i className="notika-icon notika-support"></i>Products</a>
                                </li>
                            </ul>
                            <div className="tab-content custom-menu-content">
                                <div id="Home" className="tab-pane in active notika-tab-menu-bg animated flipInX">
                                    <ul className="notika-main-menu-dropdown">
                                        <li><Link to="/dashboard">Dashboard</Link>
                                        </li>
                                    </ul>
                                </div>
                                <div id="profile" className="tab-pane notika-tab-menu-bg animated flipInX">
                                    <ul className="notika-main-menu-dropdown">
                                        <li><Link to="/user-profile">User Profile</Link>
                                        </li>
                                    </ul>
                                </div>
                                <div id="products" className="tab-pane notika-tab-menu-bg animated flipInX">
                                    <ul className="notika-main-menu-dropdown">
                                        <li><Link to="/products/category_product">Category</Link>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: partner_api.proto

package com.emporiaenergy.protos.partnerapi;

public interface OutletStatusRequestOrBuilder extends
    // @@protoc_insertion_point(interface_extends:protos.OutletStatusRequest)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>string auth_token = 1;</code>
   * @return The authToken.
   */
  java.lang.String getAuthToken();
  /**
   * <code>string auth_token = 1;</code>
   * @return The bytes for authToken.
   */
  com.google.protobuf.ByteString
      getAuthTokenBytes();

  /**
   * <code>repeated .protos.OutletStatus outlet_status = 2;</code>
   */
  java.util.List<com.emporiaenergy.protos.partnerapi.OutletStatus> 
      getOutletStatusList();
  /**
   * <code>repeated .protos.OutletStatus outlet_status = 2;</code>
   */
  com.emporiaenergy.protos.partnerapi.OutletStatus getOutletStatus(int index);
  /**
   * <code>repeated .protos.OutletStatus outlet_status = 2;</code>
   */
  int getOutletStatusCount();
  /**
   * <code>repeated .protos.OutletStatus outlet_status = 2;</code>
   */
  java.util.List<? extends com.emporiaenergy.protos.partnerapi.OutletStatusOrBuilder> 
      getOutletStatusOrBuilderList();
  /**
   * <code>repeated .protos.OutletStatus outlet_status = 2;</code>
   */
  com.emporiaenergy.protos.partnerapi.OutletStatusOrBuilder getOutletStatusOrBuilder(
      int index);
}
